import pyodbc
import datetime

CONNECTION_STRING = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:proximitydb.database.windows.net,1433;Database=Proximity;Uid=developer@proximitydb;Pwd=ProximityGroup16;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

database = pyodbc.connect(CONNECTION_STRING)

cursor = database.cursor()

def get(table):
	cursor.execute("SELECT * FROM {}".format(table))
	rows = cursor.fetchall()
	return rows

def delete(table):
	cursor.execute("DELETE FROM {}".format(table))

""" USERS """

def format_users():
	cursor.execute("DROP TABLE IF EXISTS [User]")
	cursor.execute(
		"""
		CREATE TABLE [User] (
			id INT PRIMARY KEY Identity(1,1),
			username VARCHAR(64),
			password_hash VARCHAR(128),
			latitude DECIMAL(10,8),
			longitude DECIMAL(11,8)
		)
		"""
	)

def format_friends():
	cursor.execute("DROP TABLE IF EXISTS [Friendship]")
	cursor.execute(
		"""
		CREATE TABLE [Friendship] (
			first_id INT,
			second_id INT
		)
		"""
	)

""" POSTS """

def format_posts():
	cursor.execute("DROP TABLE IF EXISTS [Post]")
	cursor.execute(
		"""
		CREATE TABLE [Post] (
			id INT PRIMARY KEY Identity(1,1),
			user_id INT,
			group_id INT,
			title VARCHAR(64),
			body TEXT,
			time DATETIME,
			latitude DECIMAL(10,8),
			longitude DECIMAL(11,8)
		)
		"""
	)

""" MESSAGES """

def format_messages():
	cursor.execute("DROP TABLE IF EXISTS [Message]")
	cursor.execute(
		"""
		CREATE TABLE [Message] (
			id INT PRIMARY KEY Identity(1,1),
			from_id INT,
			to_id INT,
			body TEXT,
			time DATETIME
		)
		"""
	)

""" GROUPS """

def format_groups():
	cursor.execute("DROP TABLE IF EXISTS [Group]")
	cursor.execute(
		"""
		CREATE TABLE [Group] (
			id INT PRIMARY KEY Identity(1,1),
			owner INT,
			name VARCHAR(32),
			private BIT,
			latitude DECIMAL(10,8),
			longitude DECIMAL(11,8)
		)
		"""
	)

""" Main Execution """

def run_tests():
	print("Users:")
	print(get("[User]"))
	query = "INSERT INTO [User] (username, password_hash) VALUES ('Nate', '12345')"
	print(query)
	cursor.execute(query)
	print(get("[User]"))
	delete("[User]")
	print(get("[User]"))

	print("\nPosts:")
	print(get("[Post]"))
	query = "INSERT INTO [Post] (user_id, title, body, time, latitude, longitude) VALUES ('0', 'Test Post', 'Please ignore', ?, 37.972811, -121.275131)"
	print(query)
	cursor.execute(query, (datetime.datetime.now(),))
	print(get("[Post]"))
	delete("[Post]")
	print(get("[Post]"))

	print("\nMessage:")
	print(get("[Message]"))
	query = "INSERT INTO [Message] (from_id, to_id, body, time) VALUES ('0', '1', 'hello', ?)"
	print(query)
	cursor.execute(query, (datetime.datetime.now(),))
	print(get("[Message]"))
	delete("[Message]")
	print(get("[Message]"))

	print("\nGroup:")
	print(get("[Group]"))
	query = "INSERT INTO [Group] (name, private) VALUES ('Test Group', 1)"
	print(query)
	cursor.execute(query)
	print(get("[Group]"))
	delete("[Group]")
	print(get("[Group]"))

	database.commit()


if __name__ == "__main__":
	# Format all tables
	format_users()
	format_posts()
	format_messages()
	format_groups()
	format_friends()

	run_tests()