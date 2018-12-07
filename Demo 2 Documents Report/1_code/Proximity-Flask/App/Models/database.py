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
			query_string = "INSERT INTO {} (username, password_hash, first_name, last_name) VALUES (?, ?, ?, ?)".format(self._config.user_table)

			cursor.execute(query_string, (user.username, user.password_hash, user.first_name, user.last_name))
			self._database.commit()

			return True

		return False


	def verify_user(self, user):
		"""
		Checks if the user credentials are valid for a user in the database
		"""
		cursor = self._database.cursor()
		query_string = "SELECT * FROM {} WHERE username = ?".format(self._config.user_table)
		print(query_string, flush=True)

		cursor.execute(query_string, (user.username,))

		row = cursor.fetchone()
		print(row, flush=True)

		if row:
			if check_password_hash(row[4], user.password):
				user.id = row[0]
				user.username = row[1]
				user.first_name = row[2]
				user.last_name = row[3]
				user.latitude = row[5]
				user.longitude = row[6]
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


	def get_user(self, user_id, latitude=None, longitude=None):
		"""
		Get a user from the database
		"""
		cursor = self._database.cursor()
		if latitude and longitude:
			print("Distance requested in user request.\nFinding distance from {} {}".format(latitude, longitude))
			query_string = "SELECT id, username, first_name, last_name, latitude, longitude, {} FROM {} WHERE id = ?".format(get_distance_string(latitude, longitude, '[User]'), '[User]')
			cursor.execute(query_string, (user_id,))
		else:
			query_string = "SELECT id, username, first_name, last_name, latitude, longitude FROM {} WHERE id = ?".format(self._config.user_table)
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


	def get_friends(self, user_id, latitude=None, longitude=None):
		"""
		Get a list of all friendships a user has
		"""
		cursor = self._database.cursor()
		query_string = "SELECT * FROM {} WHERE first_id = ? OR second_id = ?".format(self._config.friendship_table)

		cursor.execute(query_string, (user_id, user_id))
		rows = cursor.fetchall()

		print(rows, flush=True)

		friends = []

		for row in rows:
			friend = None

			if user_id != row[0]:
				friend = self.get_user(row[0], latitude, longitude)

			if user_id != row[1]:
				friend = self.get_user(row[1], latitude, longitude)

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


	# TODO: SORT AGAINST TIME
	def get_posts(self, lat, long, radius, group_id=0):
		"""
		Gets all posts made within a radius of the latitude and longitude provided
		"""
		cursor = self._database.cursor()
		query_string = "SELECT [Post].id, user_id, username, title, body, time, ( 3959 * acos( cos( radians({}) ) * cos( radians( Post.latitude ) ) * cos( radians( Post.longitude ) - radians({}) ) + sin( radians({}) ) * sin( radians( Post.latitude ) ) ) ) AS distance FROM {} INNER JOIN [User] ON Post.user_id = [User].id WHERE group_id = ? ORDER BY time DESC".format(lat, long, lat, self._config.post_table, radius)

		print(query_string, flush=True)

		cursor.execute(query_string, (group_id,))
		rows = cursor.fetchall()

		print(rows, flush=True)

		filtered_rows = []
		for row in rows:
			if row[6] < radius:
				user = User.from_row(self.get_user(row[1]))

				if user:
					row[1] = user.get_json()

					print(row[5], flush=True)

					filtered_rows.append(row)

		return filtered_rows

	def get_user_posts(self, user_id):
		"""
		Gets all posts made within a radius of the latitude and longitude provided
		"""
		cursor = self._database.cursor()
		query_string = "SELECT * FROM [Post] WHERE user_id = ?"

		cursor.execute(query_string, (user_id,))
		rows = cursor.fetchall()

		filtered_rows = []
		for row in rows:
			user = User.from_row(self.get_user(row[1]))

			if user:
				row[1] = user.get_json()
				filtered_rows.append(row)

		return filtered_rows

	def create_comment(self, comment):
		"""
		Creates a new comment in the comment database
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO [Comment] (user_id, post_id, time, body) VALUES (?,?,?,?)"

		cursor.execute(query_string, (comment.user_id, comment.post_id, datetime.datetime.now(), comment.body))
		self._database.commit()

		return True

	def get_comments(self, post_id):
		"""
		Gets all comments on a post
		"""
		cursor = self._database.cursor()
		query_string = "SELECT * FROM [Comment] WHERE post_id = ?"

		print(query_string, flush=True)

		cursor.execute(query_string, (post_id,))
		rows = cursor.fetchall()

		filtered_rows = []

		for row in rows:
			user = User.from_row(self.get_user(row[1]))

			if user:
				row[1] = user.get_json()

				filtered_rows.append(row)


		print(filtered_rows, flush=True)

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

		filtered_rows = []
		for row in rows:
			if row[6] < 100:
				filtered_rows.append(row)

		return filtered_rows


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


	""" EVENT METHODS """

	def create_event(self, event):
		"""
		Create an event in the events database
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO [Event] (owner, title, latitude, longitude, time) VALUES (?, ?, ?, ?, ?)"

		cursor.execute(query_string, (event.owner, event.title, event.latitude, event.longitude, datetime.datetime.now()))
		self._database.commit()

		return True

	def get_events(self, latitude, longitude, radius):
		"""
		Fetches all nearby events
		"""
		cursor = self._database.cursor()
		distance_string = get_distance_string(latitude, longitude, "[Event]")
		query_string = "SELECT *, {} FROM {}".format(distance_string, "[Event]")

		cursor.execute(query_string)
		rows = cursor.fetchall()

		print(rows, flush=True)

		filtered_rows = []
		for row in rows:
			if row[6] < 50:
				user_data = self.get_user(row[1])

				if user_data:
					user = User.from_row(user_data)
					row[1] = user.get_json()
					filtered_rows.append(row)

		return filtered_rows


	def create_attendee(self, attendee):
		"""
		Create a new attendee
		"""
		cursor = self._database.cursor()
		query_string = "INSERT INTO [Attendee] (event_id, user_id) VALUES (?,?)"

		cursor.execute(query_string, (attendee.event_id, attendee.user_id))
		self._database.commit()

		return True


	def get_attendees(self, event_id):
		"""
		Fecthes all attendees of an event
		"""
		cursor = self._database.cursor()
		query_string = "SELECT user_id FROM [Attendee] WHERE event_id = ?"

		cursor.execute(query_string, (event_id,))
		rows = cursor.fetchall()

		print(rows, flush=True)

		filtered_rows = []
		for row in rows:
			user_data = self.get_user(row[0])

			if user_data:
				user = User.from_row(user_data)

				filtered_rows.append(user)

		return filtered_rows


""" UTILITIES """

def get_distance_string(latitude, longitude, table_name):
	distance_string = "(3959 * acos( cos( radians({}) ) * cos( radians( {}.latitude ) ) * cos( radians( {}.longitude ) - radians({}) ) + sin( radians({}) ) * sin( radians( {}.latitude ) ) ) ) AS distance"
	return distance_string.format(latitude, table_name, table_name, longitude, latitude, table_name)