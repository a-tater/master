# import sqlite3
# import os

# def create_sqlite_database(db_filepath):
# 	try:
# 		conn = sqlite3.connect(db_filepath)
# 		print(f"SQLite database created successfully at: {db_filepath}")
# 	except sqlite3.Error as e:
# 		print(f"Error creating database: {e}")
# 	except Exception as e:
# 		print(f"An unexpected error occurred: {e}")
# 	finally:
# 		if 'conn' in locals() and conn:
# 			conn.close()

# database_name = "tti.db"
# current_directory = os.getcwd()
# database_path = os.path.join(current_directory, database_name)

# create_sqlite_database(database_path)


import util

U = util.Util('tti')

table = U.mySql("""
	select * from sam_contracts
""")

print(table)