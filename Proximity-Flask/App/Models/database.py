from werkzeug.security import check_password_hash

from App.Models.config import DefaultConfig

class DatabaseController:
	def __init__(self, database, config=None):
		if not config:
			self._config = DefaultConfig()

		self._database = database

		self._cursor = self._database.cursor()


	def create_user(self, user):
		"""
		Checks if the user account already exists, if it does not, create it
		"""
		query_string = "SELECT username FROM {} WHERE username = ?".format(self._config.user_table)

		self._cursor.execute(query_string, user.username)

		row = self._cursor.fetchone()

		if not row:
			query_string = "INSERT INTO {} (username, password_hash) VALUES (?, ?)".format(self._config.user_table)

			self._cursor.execute(query_string, (user.username, user.password_hash))

			return True

		return False


	def verify_user(self, user):
		"""
		Checks if the user credentials are valid for a user in the database
		"""
		query_string = "SELECT username, password_hash FROM {} WHERE username = ?".format(self._config.user_table)

		self._cursor.execute(query_string, user.username)

		row = self._cursor.fetchone()

		if row:
			if check_password_hash(row[1], user.password):
				return True

		return False

	""" Internal Methods """

