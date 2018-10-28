import MySQLdb
import datetime

db_conn = MySQLdb.connect(
	host="proximitydatabase.cbcqll27hw91.us-west-2.rds.amazonaws.com",
	user="admin",
	passwd="4320Group16",
	db="proximity_database"
)

cursor = db_conn.cursor()

def get(table):
	cursor.execute("SELECT * FROM {}".format(table))
	rows = cursor.fetchall()
	return rows

def delete(table):
	cursor.execute("DELETE FROM {} WHERE 1".format(table))

""" USERS """

def format_users():
	cursor.execute("DROP TABLE IF EXISTS User")
	cursor.execute(
		"""
		CREATE TABLE User (
			id INT PRIMARY KEY AUTO_INCREMENT,
			username VARCHAR(64),
			password_hash VARCHAR(128),
			latitude DECIMAL(10,8),
			longitude DECIMAL(11,8)
		)
		"""
	)

def format_friends():
	cursor.execute("DROP TABLE IF EXISTS Friendship")
	cursor.execute(
		"""
		CREATE TABLE Friendship (
			first_id INT,
			second_id INT
		)
		"""
	)

""" POSTS """

def format_posts():
	cursor.execute("DROP TABLE IF EXISTS Post")
	cursor.execute(
		"""
		CREATE TABLE Post (
			id INT PRIMARY KEY AUTO_INCREMENT,
			user_id INT,
			group_id INT,
			title VARCHAR(64),
			body TINYTEXT,
			time DATETIME,
			latitude DECIMAL(10,8),
			longitude DECIMAL(11,8)
		)
		"""
	)

""" MESSAGES """

def format_messages():
	cursor.execute("DROP TABLE IF EXISTS Message")
	cursor.execute(
		"""
		CREATE TABLE Message (
			id INT PRIMARY KEY AUTO_INCREMENT,
			from_id INT,
			to_id INT,
			body TINYTEXT,
			time DATETIME
		)
		"""
	)

""" GROUPS """

def format_groups():
	cursor.execute("DROP TABLE IF EXISTS `Group`")
	cursor.execute(
		"""
		CREATE TABLE `Group` (
			id INT PRIMARY KEY AUTO_INCREMENT,
			name VARCHAR(32),
			private BOOLEAN
		)
		"""
	)

""" Main Execution """

def run_tests():
	print("Users:")
	print(get("User"))
	query = "INSERT INTO User (username, password_hash) VALUES ('Nate', '12345')"
	print(query)
	cursor.execute(query)
	print(get("User"))
	delete("User")
	print(get("User"))

	print("\nPosts:")
	print(get("Post"))
	query = "INSERT INTO Post (user_id, title, body, time, latitude, longitude) VALUES ('0', 'Test Post', 'Please ignore', '{}', 37.972811, -121.275131)".format(datetime.datetime.now())
	print(query)
	cursor.execute(query)
	print(get("Post"))
	delete("Post")
	print(get("Post"))

	print("\nMessage:")
	print(get("Message"))
	query = "INSERT INTO Message (from_id, to_id, body, time) VALUES ('0', '1', 'hello', '{}')".format(datetime.datetime.now())
	print(query)
	cursor.execute(query)
	print(get("Message"))
	delete("Message")
	print(get("Message"))

	print("\nGroup:")
	print(get("`Group`"))
	query = "INSERT INTO `Group` (name, private) VALUES ('Test Group', 1)"
	print(query)
	cursor.execute(query)
	print(get("`Group`"))
	delete("`Group`")
	print(get("`Group`"))


if __name__ == "__main__":
	# Format all tables
	format_users()
	format_posts()
	format_messages()
	format_groups()
	format_friends()

	run_tests()