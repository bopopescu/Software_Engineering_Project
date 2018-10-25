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

def format_posts():
	cursor.execute("DROP TABLE IF EXISTS User")
	cursor.execute(
		"""
		CREATE TABLE User (
			id INT PRIMARY KEY AUTO_INCREMENT,
			username VARCHAR(64),
			password_hash VARCHAR(128)
		)
		""")

""" POSTS """

def format_users():
	cursor.execute("DROP TABLE IF EXISTS Post")
	cursor.execute(
		"""
		CREATE TABLE Post (
			id INT PRIMARY KEY AUTO_INCREMENT,
			user_id INT,
			title VARCHAR(64),
			body TINYTEXT,
			time DATETIME,
			latitude DECIMAL(10,8),
			longitude DECIMAL(11,8)
		)
		""")

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


if __name__ == "__main__":
	# Format all tables
	format_users()
	format_posts()

	run_tests()