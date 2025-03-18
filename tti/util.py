#!/usr/bin/env python3
# import boto3, json, botocore, yaml, time, os, shutil, datetime, mysql.connector, unicodedata
# from fastavro import reader, json_writer
import datetime, os, json, sqlite3#, yaml
from pandas.io import sql
# from sqlalchemy import create_engine
# from sqlalchemy import text
import pandas as pd


# AWS_REGION = 'us-east-1'
# BOTO_CONFIG = botocore.config.Config(retries={'max_attempts':10, 'mode':'adaptive'})
# AWS_ENDPOINT = '{}.console.aws.amazon.com/{{}}'.format(AWS_REGION)
pd.set_option('display.max_columns', None)

# def getEndpointUrl(resource):
# 	return 'https://{}'.format(AWS_ENDPOINT.format(resource))

# def getAWS(resource, config=BOTO_CONFIG, as_resource=False):
# 	endpoint_url = getEndpointUrl(resource)
# 	if(as_resource):
# 		return boto3.resource(resource, endpoint_url=endpoint_url, config=config, region_name=AWS_REGION)
# 	return boto3.client(resource, endpoint_url=endpoint_url, config=config, region_name=AWS_REGION)

# def getS3(config=BOTO_CONFIG, as_resource=False):
# 	return getAWS('s3', config, as_resource)

# def getEC2(config=BOTO_CONFIG, as_resource=False):
# 	return getAWS('ec2', config, as_resource)

# def getCloudFormation(config=BOTO_CONFIG, as_resource=False):
# 	return getAWS('cloudformation', config, as_resource)

# def getSecretsManager(config=BOTO_CONFIG):
# 	return getAWS('secretsmanager', config, as_resource=False)

# def getRDS(config = BOTO_CONFIG):
# 	return getAWS('rds', config = config, as_resource = False)


class Util:
	def __init__(self, project):
		self.current_directory = os.getcwd()
		self.database_name = "tti.db"
		self.database_path = os.path.join(self.current_directory, self.database_name)
		# self.boto3Session = boto3.session.Session()
		self.project = project
		self.dbWriteBucket = 'tti'
		# self.backend = 's3'
		# self.s3 = getS3()
		# self.s3Resource = getS3(as_resource=True)
		self.credentials = {}
		self.config = {}
		# self.s3Client = boto3.client('s3')
		# self.lambdaClient = boto3.client('lambda', region_name=AWS_REGION)
		# self.codeClient = boto3.client(
			# service_name='codecommit', 
			# region_name=AWS_REGION
		# )
		# self.secretsClient = self.boto3Session.client(
		# 	service_name = 'secretsmanager',
		# 	region_name = AWS_REGION
		# )
		# self.rdsSecrets = self.getSecretValue('mrclean')
		# self.database_url = f"mysql+pymysql://{self.rdsSecrets['username']}:{self.rdsSecrets['password']}@{self.rdsSecrets['host']}/{self.rdsSecrets['database']}"
		self.pd = pd
		# self.config_bucket = 'tti-config'




	def mySql(self, query, database=None, commit=True, closeConnection=True):
		connection = sqlite3.connect(self.database_name if database is None else database)
		cursor = connection.cursor()
		cursor.execute(query)
		connection.commit() if commit else None
		rows = cursor.fetchall()# if query.lower().startswith('select') else None
		return rows
		# connection.close() if closeConnection else None
		# return rows

		# engine = create_engine(self.database_url)
		# with engine.connect() as connection:
		# 	with connection.begin():
		# 		connection.execute(text(query))
		# connection.close()
		# engine.dispose()


	def writeToMySql(self, df, table, overwriteTable=False, skipCount=False, timestamp=True):
		df = self.withMetaData(df) if timestamp else df
		df.sort_index(axis=1, inplace=True)
		engine = create_engine(self.database_url)
		if not skipCount:
			print(f'count is {len(df)}')
		with engine.begin() as connection:
			df.to_sql(name=f'{table}', con=connection, if_exists='replace' if overwriteTable else 'append', index=False)
		connection.close()
		engine.dispose()
		print('successfully ' + ('overwrote ' if overwriteTable else 'appended ') + table, flush=True)


	def readFromMySql(self, query):
		engine = create_engine(self.database_url)
		df =  self.pd.read_sql_query(query, con=engine)
		engine.dispose()
		return df


	def getOutputPathPrefix(self):
		return f's3://{self.dbWriteBucket}'
	

	def moveTmpFiles(self, tmp, url):
		url = url.replace(self.getOutputPathPrefix(), '')
		self.s3Resource.Bucket(self.dbWriteBucket).objects.filter(Prefix=url+'/').delete()
		tmp = tmp.replace(self.getOutputPathPrefix(), '')
		def moveFile(k):
			k = k['Key']
			self.s3.copy({'Bucket':self.dbWriteBucket, 'key':k}, self.dbWriteBucket, k.replace(tmp, url))
			self.s3.delete_object(Bucket = self.dbWriteBucket, Key=k)
		self.iterateS3(tmp, moveFile)


	def file2String(self, f, bucket=None, encoding='utf-8'):
		bucket = self.project if bucket is None else bucket
		return self.s3Client.get_object(Bucket=bucket, Key=f)['Body'].read().decode(encoding)


	def file2Bytes(self, f, bucket=None):
		bucket = self.project if bucket is None else bucket
		return self.s3Client.get_object(Bucket=bucket, Key=f)['Body'].read()


	def deleteS3Objects(self, objects=['test/'], bucket=None):
		bucket = self.project if bucket is None else bucket
		for o in objects:
			try:
				# self.s3Resource.Bucket(bucket).objects.filter(Prefix=o).delete()
				self.s3Client.delete_object(Bucket=bucket, Key=o)
			except Exception as e:
				print(f'could not delete {bucket}/{o}')
				print(e)
				raise e


	def getSecretValue(self, name=None):
		name = self.project if name is None else name
		try:
			get_secret_value_response = self.secretsClient.get_secret_value(SecretId=name)
			response = json.loads(get_secret_value_response['SecretString'])
		except Exception as e:
			print(e)
			raise e
		return response
	

	def iterateS3(self, prefix, f, bucket=None):
		bucket = self.project if bucket is None else bucket
		ContinuationToken=None
		while(True):
			res = None
			try:
				if(ContinuationToken is None):
					res = self.s3Client.list_objects_v2(Bucket=bucket, Prefix=prefix)
				else:
					res = self.s3Client.list_objects_v2(Bucket=bucket, Prefix=prefix, ContinuationToken=ContinuationToken)
				if res is not None and res['Contents']:
					for k in res['Contents']:
						try:
							f(k['Key'])
						except Exception as e:
							print(e)
					if('NextContinuationToken' in res and len(res['NextContiuationToken']) > 0):
						ContinuationToken = res['NextContinuationToken']
					else:
						break
				else:
					break
			except Exception as e:
				print('Error in IterateS3', e)
				break


	def yaml2Dict(self, p, bucket=None):
		bucket = self.config_bucket if bucket is None else bucket
		f = self.file2Bytes(p, bucket)
		return yaml.safe_load(f)
	

	def json2Dict(self, p, bucket=None):
		bucket = self.config_bucket if bucket is None else bucket
		f = self.file2String(p, bucket)
		return json.loads(f)


	def getCredentialsS3(self, name, bucket=None):
		bucket = self.config_bucket if bucket is None else bucket
		if(name not in self.credentials):
			self.credentials[name] = self.json2Dict(f'credentials/{name}.json', bucket)
		return self.credentials[name]
	

	def getConfigS3(self, name=None, bucket=None, format='yaml'):
		bucket = self.config_bucket if bucket is None else bucket
		name = self.project if name is None else name
		if format == 'yaml':
			return self.yaml2Dict('config.yaml', bucket)[name]
		elif format == 'json':
			return self.json2Dict('config.json', bucket)[name]

	
	def getConfig(self, project=None, local=False):
		project = self.project if None else project
		if not local:
			config = self.codeClient.get_file(repositoryName='ose_cg_dlc_dt_configs', filePath='config.yaml')
			config = config['fileContent']
			config = yaml.safe_load(config)
		else:
			with open(f'../ose_cg_dlc_dt_configs/config.yaml', 'r') as config:
				config = yaml.safe_load(config)
		return config[project]


	def getSecrets(self, name):
		try:
			get_secret_value_response = self.secretsClient.get_secret_value(SecretId=name)
			if name.endswith('.pem'):
				self.credentials[name] = get_secret_value_response['SecretString']
			else:
				self.credentials[name] = json.loads(get_secret_value_response['SecretString'])
		except Exception as e:
			print(e)
			raise e
		return self.credentials[name]
	

	def bytes_to_human_readable(self, byte_count):
		units = ['B', 'KB', 'MB', 'GB', 'TB']
		unit = 0
		while byte_count >= 1024:
			byte_count /= 1024.0
			unit += 1
		return f"{byte_count:.2f} {units[unit]}"


	def uploadFileToS3(self, file, bucket, key=None, key_prefix=None, ExtraArgs=None, deleteSource=False, Print=False):
		Key = file.split('/')[-1] if key is None else key
		key = '/'.join([key_prefix, Key]) if key_prefix is not None else Key
		try:
			if(ExtraArgs is not None):
				self.s3Client.upload_file(file, Bucket=bucket, Key=key, ExtraArgs=ExtraArgs)
			else:
				self.s3Client.upload_file(file, Bucket=bucket, Key=key)
			if deleteSource:
				os.remove(file)
			if(Print):
				print(f'{file} successfully uploaded to {bucket}/{key}' + (' and deleted' if deleteSource else ""))
		except Exception as e:
			print(f'could not upload {file} to {bucket}/{key}')
			print(e)


	def uploadObjectToS3(self, object, bucket, key, ExtraArgs=None, Print=False):
		try:
			if(ExtraArgs is not None):
				self.s3Client.upload_fileobj(object, Bucket=bucket, Key=key, ExtraArgs=ExtraArgs)
			else:
				self.s3Client.upload_fileobj(object, Bucket=bucket, Key=key)
			if(Print):
				print(f'{object} successfully uploaded to {bucket}/{key}')
		except Exception as e:
			print(f'could not upload {object} to {bucket}/{key}')
			print(e)


	def uploadFolderToS3(self, folder, bucket, key=None, deleteSource=False, Print=False):
		import s3fs
		s3_file = s3fs.S3FileSystem()
		key = folder if key is None else key
		try:
			s3_file.put(folder, f'{bucket}/{key}', recursive=True)
			if deleteSource:
				try:
					shutil.rmtree(folder, ignore_errors=True)
					print(f'successfully uploaded {folder} to {bucket}/{key} and removed {folder}') if Print else None
				except Exception as e:
					print(f'successfully uploaded {folder} to {bucket}/{key} but could not remove {folder}')
					print(e)
			else:
				print(f'successfully uploaded {folder} to {bucket}/{key}') if Print else None

		except Exception as e:
			print(f'could not upload {folder} to {bucket}/{key}')
			print(e)
		

	def uploadFolderRecursiveToS3(self, folder, bucket, key_prefix=None, deleteSource=False, Print=False, extraArgs=None):
		for root, dirs, files in os.walk(folder):
			for file in files:
				file_path = os.path.join(root, file)
				self.uploadFileToS3(file_path, bucket, file_path, key_prefix, extraArgs, deleteSource, Print)


	def deleteOlderThan(self, directory, days, top_down=False, extension=None, mkdir=True):
		import pathlib, glob
		pathlib.Path(directory).mkdir(parents=mkdir,exist_ok=True)
		print(f"Deleting files older than {days} days")
		oldest = time.time() - days*86400
		if(top_down):
			for (root,dirs,files) in os.walk(directory, topdown=True):
				for f in files:
					file_path=os.path.join(root, f)
					file_time = os.stat(file_path).st_mtime
					if(file_time < oldest):
						if extension is not None:
							if (file_path.endswith(f".{extension.replace('.','')}")):
								os.remove(file_path)
						else:
							os.remove(file_path)
		else:
			if extension is None:
				for f in glob.glob(f"{directory}/*"):
					file_time = os.stat(f).st_mtime
					if(file_time < oldest):
						os.remove(f)
			else:
				for f in glob.glob(f"{directory}/*.{extension.replace('.','')}"):
					file_time = os.stat(f).st_mtime
					if(file_time < oldest):
						os.remove(f)

	def getGsClient(self, endpoint_url=None, aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
		if endpoint_url is None or aws_access_key_id is None or aws_secret_access_key is None:
			secrets = self.getSecrets(self.project)
		endpoint_url=secrets['endpoint_url'] if endpoint_url is None else endpoint_url
		aws_access_key_id=secrets['aws_access_key_id'] if aws_access_key_id is None else aws_access_key_id
		aws_secret_access_key = secrets['aws_secret_access_key'] if aws_secret_access_key is None else aws_secret_access_key
		region_name = 'auto' if region_name is None else region_name
	
		return boto3.client("s3",
			region_name=region_name,
			endpoint_url=endpoint_url,
			aws_access_key_id=aws_access_key_id,
			aws_secret_access_key=aws_secret_access_key
		)

	def getKeys(self, source_bucket, key_prefix=None, local_bucket=None, key=None, s3Client=None, full_keys=False, file_type=None):
		s3Client = self.s3Client if s3Client is None else s3Client

		def getS3Keys(bucket=source_bucket, key_prefix=key_prefix, s3Client=s3Client):
			keys = []
			kwargs = {'Bucket': bucket, 'Prefix': key_prefix} if key_prefix is not None else {'Bucket': bucket}

			while True:
				resp = s3Client.list_objects_v2(**kwargs)
				for obj in resp['Contents']:
					if file_type is None or obj['Key'].endswith(f".{file_type.replace('.','')}"):
						keys.append(obj['Key'])
				try:
					kwargs['ContinuationToken'] = resp['NextContinuationToken']
				except KeyError:
					break
			return keys

		def getFullKeys(keys, s3Client=s3Client):
			key_list = {}
			for k in keys:
				response = s3Client.head_object(Bucket=source_bucket, Key=k)
				key_list[k] = response
			return key_list

		keys = getS3Keys()
		if full_keys:
			keys = getFullKeys(keys)
			
		if local_bucket is not None:
			s3object = boto3.resource('s3').Object(local_bucket if local_bucket is not None else source_bucket, key if key is not None else f'{source_bucket}/{key_prefix if key_prefix is not None else source_bucket}_keys')
			s3object.put(
				Body=(bytes(json.dumps(keys, indent=4, sort_keys=True, default=str).encode('UTF-8')))
			)
		return keys


	def downloadFromS3(self, bucket, key, localDir=None, fileName=None, client=None, Print=True):
		client = self.s3Client if client is None else client
		fileName = key.split('/')[-1] if fileName is None else fileName
		file = '/'.join([localDir,fileName]) if localDir is not None else fileName
		try:
			client.download_file(bucket, key, file)
			print(f"Successfully downloaded {key} from {bucket} to {file}") if Print else None
		except Exception as e:
			print(f'Failed downlaod from {bucket}/{key}: {e}')

		return file


	def getSize(self, path):
		if os.path.isfile(path):
			return os.path.getsize(path)
		elif os.path.isdir(path):
			total_size = 0
			for item in os.listdir(path):
				item_path = os.path.join(path, item)
				total_size += self.getSize(item_path)
			return total_size
		else:
			return 0


	def unPack(self, File, outDir=None, recursive=False):
		import patoolib, zipfile, os, pathlib
		if File.endswith('.zip'):
			file = zipfile.ZipFile(File)
			if outDir is not None:
				file.extractall(path=outDir)
				os.remove(File)
				if recursive:
					for f in os.listdir(outDir):
						newFile = f'{outDir}/{f}'
						newDir = f"{outDir}/{f.split('.')[0]}_zip"
						size = self.getSize(newFile)
						if size > 1024 ** 2:
							self.unPack(newFile, newDir, recursive=recursive)
			else:
				file.extractall(path=File.split('.')[0])
		elif File.endswith('.rar'):
			if outDir is not None:
				patoolib.extract_archive(File, outdir=outDir)
				os.remove(file)
				if recursive:
					for f in os.listdir(outDir):
						newFile = f'{outDir}/{f}'
						newDir = f"{outDir}/{f.split('.')[0]}"
						self.unPack(newFile, newDir, recursive=recursive)
			else:
				patoolib.extract_archive(File)
		elif pathlib.Path(File).is_dir():
			for f in os.listdir(File):
				newFile = f"{File}/{f}"
				newDir = f"{File}/{f.split('.')[0]}"
				size = self.getSize(newFile)
				if size > 1024 ** 2:
					self.unPack(newFile, newDir, recursive=recursive)



	def unpackFromS3(self, source_bucket, source_key, destination_bucket=None, destination_key=None, destination_key_prefix=None, s3Client=None, Print=True, deleteSource=True, recursive=False, extraArgs=None):
		import zipfile
		destination_key = source_key.split('.')[0].replace(' ', '_') if destination_key is None else destination_key
		s3Client = self.s3Client if s3Client is None else s3Client

		localZipDir = f'zip'
		localUnzipDir = f"{source_key.split('/')[-1].split('.')[0].replace(' ', '_')}"
		zipFile = f"{localZipDir}/{source_key.split('/')[-1].replace(' ', '_')}"

		os.makedirs(localZipDir, exist_ok=True)
		os.makedirs(localUnzipDir, exist_ok=True)
		self.downloadFromS3WithCallback(source_bucket, source_key, fileName=zipFile, client=s3Client)

		self.unPack(zipFile, localUnzipDir, recursive=recursive)

		if destination_bucket is not None:
			if recursive:
				self.uploadFolderRecursiveToS3(localUnzipDir, destination_bucket, destination_key_prefix, deleteSource=deleteSource, Print=Print, extraArgs=extraArgs)
			else:
				self.uploadFolderToS3(localUnzipDir, destination_bucket, localUnzipDir, deleteSource, Print)

		if deleteSource:
			shutil.rmtree(localZipDir, ignore_errors=True)
	

	def avroToJson(self, source_bucket, source_key, destination_bucket=None, key_prefix=None, destination_key=None, s3Client=None, Print=True, deleteSource=True):
		s3Client = self.s3Client if s3Client is None else s3Client

		localAvroDir = 'avro'
		localJsonDir = 'json'
		avroFile = f"{source_key.split('/')[-1].split('.')[0].replace(' ', '_')}"
		destination_key = avroFile if destination_key is None else destination_key

		os.makedirs(localAvroDir, exist_ok=True)
		os.makedirs(localJsonDir, exist_ok=True)
		self.downloadFromS3(source_bucket, source_key, fileName=f'{localAvroDir}/{avroFile}', client=s3Client)

		with open(f'{localJsonDir}/{avroFile}', 'w') as json_file:
			with open(f'{localAvroDir}/{avroFile}', 'rb') as avro_file:
				avro_reader = reader(avro_file)
				json_writer(json_file, avro_reader.writer_schema, avro_reader)
		
		key = f'{key_prefix}/{destination_key}' if key_prefix is not None else destination_key

		if destination_bucket is not None:
			self.uploadFileToS3(f"{localJsonDir}/{avroFile}", destination_bucket, key, deleteSource=deleteSource, Print=Print)

		shutil.rmtree(localAvroDir, ignore_errors=True)

	
	def iterate(self, f, start, interval, end=datetime.datetime.now(), tz=datetime.timezone.utc):
		stat = self.generateStat()
		stat['current_start'] = start
		print(stat['current_start'])

		while stat['current_start'] < end:
			stat['current_end'] = min(end, (stat['current_start'] + interval))
			print(f"""Running: for range {stat['current_start'].strftime('%Y-%m-%d')} to {stat['current_end'].strftime('%Y-%m-%d')}""")
			f(stat)

			stat['current_start'] += interval
		print(f'Interval Complete')


	def generateStat(self):
		return {'start':datetime.datetime.now(datetime.timezone.utc)}


	def getMagicType(self, object):
		import magic
		object = object['Body'].read()
		return magic.from_buffer(object, mime=True)
	

	def getPureMagicType(self, object):
		import puremagic
		object = object['Body'].read()
		return puremagic.magic_string(object)[0].mime_type
	

	def withMetaData(self, df):
		df['ose_timestamp'] = self.pd.Timestamp("now")
		return df

	def found_in_s3(self, bucket, key, s3Client=None):
		s3Client = self.s3Client if s3Client is None else s3Client
		try:
			s3Client.head_object(Bucket=bucket, Key=key)
			return True
		except:
			return False

	def normalize_string(self, input_string):
		normalized_string = unicodedata.normalize('NFKD', input_string)
		ascii_string = normalized_string.encode('ascii', 'ignore')

		return ascii_string.decode('ascii')


	def print(self, *args):
		print(*args, flush=True)


	class TransferCallback:
		def __init__(self, target_size, Print=True):
			self._target_size = target_size
			self._total_transferred = 0
			self._lock = threading.Lock()
			self.thread_info = {}
			self.Print = Print

		def __call__(self, bytes_transferred):
			thread = threading.current_thread()
			with self._lock:
				self._total_transferred += bytes_transferred
				if thread.ident not in self.thread_info.keys():
					self.thread_info[thread.ident] = bytes_transferred
				else:
					self.thread_info[thread.ident] += bytes_transferred

				target = self._target_size
				if self.Print:
					print(
						f"\r{self._total_transferred} of {target} transferred ",
						f"({(self._total_transferred / target) * 100:.2f}%).",
					flush=True)


	def downloadFromS3WithCallback(self, bucket, key, file_size=None, localDir=None, fileName=None, client=None, Print=True):
		client = self.s3Client if client is None else client
		file_size = self.getKeys(bucket, key, full_keys=True)[key].get('ContentLength') if file_size is None else file_size
		fileName = key.split('/')[-1] if fileName is None else fileName
		file = '/'.join([localDir,fileName]) if localDir is not None else fileName
		transfer_callback = self.TransferCallback(file_size, Print)

		try:
			client.download_file(bucket, key, file, Callback=transfer_callback)
		except Exception as e:
			print(f'Failed downlaod from {bucket}/{key}: {e}')	

		return file
	

	def downloadFromS3(self, bucket, key, localDir=None, fileName=None, client=None, Print=True):
		client = self.s3Client if client is None else client
		fileName = key.split('/')[-1] if fileName is None else fileName
		file = '/'.join([localDir,fileName]) if localDir is not None else fileName
		try:
			client.download_file(bucket, key, file)
			print(f"Successfully downloaded {key} from {bucket} to {file}") if Print else None
		except Exception as e:
			print(f'Failed downlaod from {bucket}/{key}: {e}')

		return file