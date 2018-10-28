import datetime

from werkzeug.security import check_password_hash

from App.Models import (
	User,
	DefaultConfig
)

class DatabaseController:
	def __init__(self, database, config=None):
		if not config:
			config = DefaultConfig()

		self._config = config
		self._database = database

		self._cursor = self._database.cursor()


	""" User Methods """

	def create_user(self, user):
		"""
		Checks if the user account already exists, if it does not, create it
		"""
		query_string = "SELECT username FROM {} WHERE username = %s".format(self._config.user_table)
		print(query_string)

		self._cursor.execute(query_string, (user.username,))

		row = self._cursor.fetchone()
		print(row)

		if not row:
			query_string = "INSERT INTO {} (username, password_hash) VALUES (%s, %s)".format(self._config.user_table)

			self._cursor.execute(query_string, (user.username, user.password_hash))
			self._database.commit()

			return True

		return False


	def verify_user(self, user):
		"""
		Checks if the user credentials are valid for a user in the database
		"""
		query_string = "SELECT id, username, password_hash FROM {} WHERE username = %s".format(self._config.user_table)
		print(query_string)

		self._cursor.execute(query_string, (user.username,))

		row = self._cursor.fetchone()
		print(row)

		if row:
			if check_password_hash(row[2], user.password):
				user._id = row[0]
				return True

		return False


	def update_user(self, user, username=None, password=None):
		"""
		Changes the user's credentials to the new credentials given
		"""
		if password:
			updated_user = User(username=username, password=password)

			query_string = "UPDATE {} SET password_hash=%s WHERE username=%s".format(self._config.user_table)

			self._cursor.execute(query_string, (updated_user.password_hash, user.username))

		if username:
			query_string = "UPDATE {} SET username=%s WHERE username=%s".format(self._config.user_table)

			self._cursor.execute(query_string, (user.username, user.username))

		self._database.commit()

		return True


	def update_user_location(self, user_id, latitude, longitude):
		"""
		Updates the user's most recent location
		"""
		query_string = "UPDATE {} SET latitude = %s, longitude = %s WHERE id = %s".format(self._config.user_table)
		# print("{} {}".format(latitude, longitude))
		self._cursor.execute(query_string , (latitude, longitude, user_id))
		self._database.commit()

		return True


	def get_user(self, user_id):
		"""
		Get a user from the database
		"""
		query_string = "SELECT id, username, latitude, longitude FROM {} WHERE id = %s".format(self._config.user_table)
		self._cursor.execute(query_string, (user_id,))
		row = self._cursor.fetchone()

		print(row)

		return row

	""" Friendship Methods """

	def new_friendship(self, friendship):
		"""
		Add a new friendship
		"""
		query_string = "INSERT INTO {} (first_id, second_id) VALUES (%s, %s)".format(self._config.friendship_table)

		if friendship.user_one > friendship.user_two:
			first = friendship.user_two
			second = friendship.user_one
		else:
			first = friendship.user_one
			second = friendship.user_two

		self._cursor.execute(query_string, (first, second))
		self._database.commit()

		return True


	def get_friends(self, user_id):
		"""
		Get a list of all friendships a user has
		"""
		query_string = "SELECT * FROM {} WHERE first_id = %s OR second_id = %s".format(self._config.friendship_table)

		self._cursor.execute(query_string, (user_id, user_id))
		rows = self._cursor.fetchall()

		friends = []

		for row in rows:
			friend = None

			if user_id != row[0]:
				friend = self.get_user(row[0])

			if user_id != row[1]:
				friend = self.get_user(row[1])

			if friend:
				friends.append(friend)


		print(friends)

		return friends


	""" Post Methods """

	def create_post(self, post, group_id=0):
		"""
		Creates a new post in the post database
		"""
		query_string = "INSERT INTO {} (user_id, group_id, title, body, time, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s, %s)".format(self._config.post_table)

		self._cursor.execute(query_string, (post.user_id, group_id, post.title, post.body, datetime.datetime.now(), post.latitude, post.longitude))
		self._database.commit()

		return True


	def get_posts(self, lat, long, radius, group_id=0):
		"""
		Gets all posts made within a radius of the latitude and longitude provided
		"""
		query_string = "SELECT user_id, username, title, body, time, ( 3959 * acos( cos( radians({}) ) * cos( radians( latitude ) ) * cos( radians( longitude ) - radians({}) ) + sin( radians({}) ) * sin( radians( latitude ) ) ) ) AS distance FROM {} INNER JOIN User ON Post.user_id = User.id WHERE group_id = %s HAVING distance < {} ORDER BY distance".format(lat, long, lat, self._config.post_table, radius)

		print(query_string)

		self._cursor.execute(query_string, (group_id,))
		rows = self._cursor.fetchall()

		print(rows)

		return rows


	""" Message Methods """

	def send_message(self, message):
		"""
		Creates a new message in the message database
		"""
		query_string = "INSERT INTO {} (from_id, to_id, body, time) VALUES (%s, %s, %s, %s)".format(self._config.message_table)

		self._cursor.execute(query_string, (message.from_id, message.to_id, message.body, datetime.datetime.now()))
		self._database.commit()

		return True


	def get_messages(self, to_id=None, from_id=None):
		"""
		Gets all messages with the given ids
		"""
		query_string = """
			SELECT from_id, to_id, body, time FROM {} 
		""".format(self._config.message_table)

		rows = None

		if to_id != None and from_id == None:
			query_string += " WHERE to_id = %s"
			self._cursor.execute(query_string, (to_id,))
			rows = self._cursor.fetchall()

		elif to_id == None and from_id != None:
			query_string += " WHERE from_id = %s"
			self._cursor.execute(query_string, (from_id,))
			rows = self._cursor.fetchall()

		elif to_id != None and from_id != None:
			query_string += " WHERE to_id = %s AND from_id = %s"
			self._cursor.execute(query_string, (to_id, from_id))
			rows = self._cursor.fetchall()

		else:
			self._cursor.execute(query_string)
			rows = self._cursor.fetchall()

		return rows


	""" Group Methods """

	def create_group(self, group):
		"""
		Creates a new group in the group database
		"""
		query_string = "INSERT INTO {} (name, private) VALUES (%s, %s)".format(self._config.group_table)

		self._cursor.execute(query_string, (group.name, group.private))
		self._database.commit()

		return True