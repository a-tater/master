import requests, sqlite3
import pandas as pd

def make_api_request(url, api_key, params=None):
	headers = {	
		"X-API-Key": api_key,
		"Content-Type": "application/json"
	}
	try:
		response = requests.get(url, headers=headers, params=params)
		response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
		return response.json()
	except requests.exceptions.RequestException as e:
		print(f"Error making API request: {e}")
		if response is not None:
			try:
				print(f"Response Content: {response.text}")
			except:
				print("Could not display response text")
		return None
	except ValueError as e: # Catch if json decoding fails
		print(f"Error decoding JSON response: {e}")
		if response is not None:
			try:
				print(f"Response Content: {response.text}")
			except:
				print("Could not display response text")
		return None
	except Exception as e: # Catch any other errors
		print(f"An unexpected error occured: {e}")
		return None


""" info can be located here https://open.gsa.gov/api/get-opportunities-public-api/ """

api_url = "https://api.sam.gov/opportunities/v2/search"
api_key = "YRAXnizfe51nj9O9lCtNKUpSzRVJf440MdojRMvS"
query_params = {
	"postedFrom": "01/01/2025", 
	"postedTo": "12/31/2025",
	"typeOfSetAside": "SDVOSBC",
	"ptype": [
		"u", # = Justification (J&A)
		"p", # = Pre solicitation
		# "a", # = Award Notice
		"r", # = Sources Sought
		# "s", # = Special Notice
		"o", # = Solicitation
		# "g", # = Sale of Surplus Property
		"k" #, # = Combined Synopsis/Solicitation
		# "i"  # = Intent to Bundle Requirements (DoD-Funded)
	],
	"limit": 1000
}

data = make_api_request(api_url, api_key, query_params)
dataList = []

def makeRows(data, offset=0):
	count = data["totalRecords"]
	records = data['opportunitiesData']
	for record in records:
		dataList.append({
			"desc_url" : record.get('description'),
			"id" : record.get('noticeId'),
			"title" : record.get('title'),
			"solicitationNumber" : record.get('solicitationNumber'),
			"agencies" : record.get('fullParentPathName'),
			"department" : record.get('department'),
			"postedDate" : record.get('postedDate'),
			"ptype" : record.get('type'),
			"setaside" : record.get('typeOfSetAside'),
			"dueDate" : record.get('responseDeadLine'),
			"naicsCode" : record.get('naicsCode'),
			"active" : True if record.get('active') == 'Yes' else False,
			# "location" : record.get('placeOfPerformance'),
			# "poc" : record.get('officeAddress'),
			# "links" : record.get('links'),
			# "resources" : record.get('resourceLinks'),
			"addl_info" : record.get('additionalInfoLink'),
			"classCode" : record.get('classificationCode')
		})
	if (count - offset) > 1000:
		offset += 1000
		query_params['offset'] = offset
		data = make_api_request(api_url, api_key, query_params)
		makeRows(data, offset)

makeRows(data)

print(f'count is {len(dataList)}')
quit()





def create_table_from_list_of_dicts(db_filepath, table_name, data_list):
	try:
		conn = sqlite3.connect(db_filepath)
		cursor = conn.cursor()

		if not data_list:
			print("Data list is empty. No table created.")
			return

		# Get the keys from the first dictionary to create the table schema
		columns = ", ".join([f"{key} TEXT" for key in data_list[0].keys()]) # All columns as text for simplicity
		create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
		cursor.execute(create_table_query)

		# Insert data from each dictionary into the table
		for data_dict in data_list:
			placeholders = ", ".join(["?" for _ in data_dict.values()])
			insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
			cursor.execute(insert_query, tuple(data_dict.values()))

		conn.commit()
		print(f"Table '{table_name}' created and data inserted successfully.")

	except sqlite3.Error as e:
		print(f"SQLite error: {e}")
	except Exception as e:
		print(f"An error occurred: {e}")
	finally:
		if 'conn' in locals() and conn:
			conn.close()


db_file = "tti.db"
table_name = "sam_contracts"

create_table_from_list_of_dicts(db_file, table_name, dataList)


# create_table_from_list_of_dicts(db_file, table_name, data):
# 	try:
# 		conn = sqlite3.connect(db_file)
# 		cursor = conn.cursor()
# 		cursor.execute(f"SELECT * FROM {table_name}")
# 		results = cursor.fetchall()
# 		print("\nTable contents:")
# 		for row in results:
# 			print(row)
# 	except sqlite3.Error as e:
# 		print(f"SQLite error: {e}")
# 	finally:
# 		if 'conn' in locals() and conn:
# 			conn.close()

# #Example empty list
# create_table_from_list_of_dicts(db_file, "empty_table", [])