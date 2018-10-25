import MySQLdb

db_conn = MySQLdb.connect(
	host="proximitydatabase.cbcqll27hw91.us-west-2.rds.amazonaws.com",
	user="admin",
	passwd="4320Group16",
	db="proximity_database"
)

cursor = db_conn.cursor()

def get_users():
	cursor.execute("SELECT * FROM User")
	rows = cursor.fetchall()
	return rows

def delete_users():
	cursor.execute("DELETE FROM User WHERE 1")

def run_tests():
	print(get_users())
	print("INSERT INTO User (username, password_hash) VALUES ('Nate', '12345')")
	cursor.execute("INSERT INTO User (username, password_hash) VALUES ('Nate', '12345')")
	print(get_users())
	delete_users()
	print(get_users())


if __name__ == "__main__":
	cursor.execute("DROP TABLE IF EXISTS User")

	cursor.execute(
		"""
		CREATE TABLE User (
			id INT PRIMARY KEY,
			username VARCHAR(64),
			password_hash VARCHAR(128)
		)
		""")

	run_tests()