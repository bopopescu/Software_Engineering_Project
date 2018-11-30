import datetime
import MySQLdb
import pyodbc

from werkzeug.security import check_password_hash

from App.Models import (
	User,
	DefaultConfig
)

CONNECTION_STRING = "Driver={ODBC Driver 17 for SQL Server};Server=tcp:proximitydb.database.windows.net,1433;Database=Proximity;Uid=developer@proximitydb;Pwd=ProximityGroup16;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

class DatabaseController:
	def __init__(self, database=None, config=None):
		if not config:
			config = DefaultConfig()

		self._config = config

		if not database:
			# database = MySQLdb.connect(
			# 	host = self._config.host,
			# 	user = self._config.user,
			# 	passwd = self._config.password,
			# 	db = self._config.database
			# )
			database = pyodbc.connect(CONNECTION_STRING)

		self._database = database

	""" User Methods """

	def create_user(self, user):
		"""
		Checks if the user account already exists, if it does not, create it
		"""
		cursor = self._database.cursor()
		query_string = "SELECT username FROM {} WHERE username = ?".format(self._config.user_table)
		print(query_string, flush=True)

		cursor.execute(query_string, (user.username,))

		row = cursor.fetchone()
		print(row, flush=True)

		if not row:
			query_string = "INSERT INTO {} (username, password_hash) VALUES (?, ?)".format(self._config.user_table)

			cursor.execute(query_string, (user.username, user.password_hash))
			self._database.commit()

			return True

		return False


	def verify_user(self, user):
		"""
		Checks if the user credentials are valid for a user in the database
		"""
		cursor = self._database.cursor()
		query_string = "SELECT id, username, password_hash FROM {} WHERE username = ?".format(self._config.user_table)
		print(query_string, flush=True)

		cursor.execute(query_string, (user.username,))

		row = cursor.fetchone()
		print(row, flush=True)

		if row:
			if check_password_hash(row[2], user.password):
				user._id = row[0]
				return True

		return False


	def update_user(self, user, username=None, password=None):
		"""
		Changes the user's credentials to the new credentials given
		"""
		cursor = self._database.cursor()
		if password:
			updated_user = User(username=username, password=password)

			query_string = "UPDATE {} SET password_hash=? WHERE username=?".format(self._config.user_table)

			cursor.execute(query_string, (updated_user.password_hash, user.username))

		if username:
			query_string = "UPDATE {} SET username=? WHERE username=?".format(self._config.user_table)

			cursor.execute(query_string, (user.username, user.username))

		self._database.commit()

		return True


	def update_user_location(self, user_id, latitude, longitude):
		"""
		Updates the user's most recent location
		"""
		cursor = self._database.cursor()
		query_string = "UPDATE {} SET latitude = ?, longitude = ? WHERE id = ?".format(self._config.user_table)
		# print("{} {}".format(latitude, longitude))
		cursor.execute(query_string, (latitude, longitude, user_id))
		self._database.commit()

		return True


	def get_user(self, user_id):
		"""
		Get a user from the database
		"""
		cursor = self._database.cursor()
		query_string = "SELECT id, username, latitude, longitude FROM {} WHERE id = ?".format(self._config.user_table)
		cursor.execute(query_string, (user_id,))
		row = cursor.fetchone()

		print(row, flush=True)

		return row

	""" Friendship Methods """

	def new_friendship(self, friendship):
		"""
		Add a new friendship
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO {} (first_id, second_id) VALUES (?, ?)".format(self._config.friendship_table)

		if friendship.user_one > friendship.user_two:
			first = friendship.user_two
			second = friendship.user_one
		else:
			first = friendship.user_one
			second = friendship.user_two

		cursor.execute(query_string, (first, second))
		self._database.commit()

		return True


	def get_friends(self, user_id):
		"""
		Get a list of all friendships a user has
		"""
		cursor = self._database.cursor()
		query_string = "SELECT * FROM {} WHERE first_id = ? OR second_id = ?".format(self._config.friendship_table)

		cursor.execute(query_string, (user_id, user_id))
		rows = cursor.fetchall()

		friends = []

		for row in rows:
			friend = None

			if user_id != row[0]:
				friend = self.get_user(row[0])

			if user_id != row[1]:
				friend = self.get_user(row[1])

			if friend:
				friends.append(friend)


		print(friends, flush=True)

		return friends


	""" Post Methods """

	def create_post(self, post, group_id=0):
		"""
		Creates a new post in the post database
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO {} (user_id, group_id, title, body, time, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?, ?)".format(self._config.post_table)

		cursor.execute(query_string, (post.user_id, group_id, post.title, post.body, datetime.datetime.now(), post.latitude, post.longitude))
		self._database.commit()

		return True


	def get_posts(self, lat, long, radius, group_id=0):
		"""
		Gets all posts made within a radius of the latitude and longitude provided
		"""
		cursor = self._database.cursor()
		query_string = "SELECT user_id, username, title, body, time, ( 3959 * acos( cos( radians({}) ) * cos( radians( Post.latitude ) ) * cos( radians( Post.longitude ) - radians({}) ) + sin( radians({}) ) * sin( radians( Post.latitude ) ) ) ) AS distance FROM {} INNER JOIN [User] ON Post.user_id = [User].id WHERE group_id = ?".format(lat, long, lat, self._config.post_table, radius)

		print(query_string, flush=True)

		cursor.execute(query_string, (group_id,))
		rows = cursor.fetchall()

		print(rows, flush=True)

		filtered_rows = []
		for row in rows:
			if row[5] < radius:
				filtered_rows.append(row)

		return filtered_rows


	""" Message Methods """

	def send_message(self, message):
		"""
		Creates a new message in the message database
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO {} (from_id, to_id, body, time) VALUES (?, ?, ?, ?)".format(self._config.message_table)

		cursor.execute(query_string, (message.from_id, message.to_id, message.body, datetime.datetime.now()))
		self._database.commit()

		return True


	def get_messages(self, to_id=None, from_id=None):
		"""
		Gets all messages with the given ids
		"""
		cursor = self._database.cursor()
		query_string = """
			SELECT from_id, to_id, body, time FROM {} 
		""".format(self._config.message_table)

		rows = None

		if to_id != None and from_id == None:
			query_string += " WHERE to_id = ?"
			cursor.execute(query_string, (to_id,))
			rows = cursor.fetchall()

		elif to_id == None and from_id != None:
			query_string += " WHERE from_id = ?"
			cursor.execute(query_string, (from_id,))
			rows = cursor.fetchall()

		elif to_id != None and from_id != None:
			query_string += " WHERE to_id = ? AND from_id = ?"
			cursor.execute(query_string, (to_id, from_id))
			rows = cursor.fetchall()

		else:
			cursor.execute(query_string)
			rows = cursor.fetchall()

		print(rows, flush=True)

		return rows


	""" Group Methods """

	def create_group(self, group):
		"""
		Creates a new group in the group database
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO {} (owner, name, private, latitude, longitude) VALUES (?, ?, ?, ?, ?)".format(self._config.group_table)

		cursor.execute(query_string, (group.owner, group.name, group.private, group.latitude, group.longitude))
		self._database.commit()

		return True


	def get_groups(self, lat, long):
		"""
		Fetches a list of groups that were created nearby
		"""
		cursor = self._database.cursor()
		distance_string = get_distance_string(lat, long, "[Group]")
		query_string = "SELECT *, {} FROM {}".format(distance_string, "[Group]")

		cursor.execute(query_string)
		rows = cursor.fetchall()

		print(rows, flush=True)

		# filtered_rows = []
		# for row in rows:
		# 	if row[5] < 50:
		# 		filtered_rows.append(row)

		return rows


	def delete_group(self, group_id):
		"""
		Deletes a group from the group table
		"""
		cursor = self._database.cursor()

		query_string = "DELETE FROM {} WHERE id = ?".format("[Group]")

		cursor.execute(query_string, (group_id,))
		cursor.commit()

		return True


	def get_group(self, group_id):
		"""
		Fetches all the info on a single group based on its ID
		"""
		cursor = self._database.cursor()
		query_string = "SELECT * FROM {} WHERE id = ?".format("[Group]")

		cursor.execute(query_string, (group_id,))

		row = cursor.fetchone()

		return row


""" UTILITIES """

def get_distance_string(latitude, longitude, table_name):
	distance_string = "(3959 * acos( cos( radians({}) ) * cos( radians( {}.latitude ) ) * cos( radians( {}.longitude ) - radians({}) ) + sin( radians({}) ) * sin( radians( {}.latitude ) ) ) ) AS distance"
	return distance_string.format(latitude, table_name, table_name, longitude, latitude, table_name)