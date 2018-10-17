import jwt
from werkzeug.security import generate_password_hash

from App.Models.config import DefaultConfig

class User:
	"""
	Represents a user in the database with functionality for creating and verifying accounts
	"""
	def __init__(self, username, password):
		self._username = username
		self._password = password
		self._password_hash = generate_password_hash(password)


	def get_token(self):
		private_key = DefaultConfig.get_private_key()
		
		data = self.get_json()
		token = jwt.encode(data, private_key, algorithm='RS256')

		return token


	def get_json(self):
		"""
		Returns a json of all user data
		Currently it's just the username, but who knows what else it will hold in the future
		"""
		return {
			"username": self.username
		}


	@property
	def username(self):
		return self._username


	@property
	def password(self):
		return self._password


	@property
	def password_hash(self):
		return self._password_hash