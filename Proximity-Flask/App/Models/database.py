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



	""" Post Methods """

	def create_post(self, post):
		"""
		Creates a new post in the post database
		"""
		query_string = "INSERT INTO {} (user_id, title, body, time, latitude, longitude) VALUES (%s, %s, %s, %s, %s, %s)".format(self._config.post_table)

		self._cursor.execute(query_string, (post.user.id, post.title, post.body, datetime.datetime.now(), post.latitude, post.longitude))
		self._database.commit()

		return True


	def get_posts(self, lat, long, radius):
		"""
		Gets all posts made within a radius of the latitude and longitude provided
		"""
		query_string = """
			SELECT id, user_id, title, body, ( 3959 * acos( cos( radians({}) ) * cos( radians( latitude ) ) * cos( radians( longitude ) - radians({}) ) + sin( radians({}) ) * sin( radians( latitude ) ) ) ) AS distance FROM {} HAVING distance < {} ORDER BY distance LIMIT 0 , 20
		""".format(lat, long, lat, self._config.post_table, radius)
		
		self._cursor.execute(query_string)

		rows = self._cursor.fetchall()

		return rows
