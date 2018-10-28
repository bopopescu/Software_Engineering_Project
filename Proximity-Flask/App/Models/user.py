import jwt
from werkzeug.security import generate_password_hash

from App.Models.config import DefaultConfig
from App.Models import _BaseModel

class User(_BaseModel):
	"""
	Represents a user in the database with functionality for creating and verifying accounts
	"""
	def __init__(self, id=None, username=None, latitude=None, longitude=None, password=None, config=None, scope=None):
		self._id = id
		self._username = username
		self._latitude = latitude
		self._longitude = longitude

		self._password = password
		self._scope = scope

		if password:
			self._password_hash = generate_password_hash(password)

		if not config:
			config = DefaultConfig()

		self._config = config


	def get_token(self, scope):
		private_key = DefaultConfig.get_private_key()
		
		data = self.get_json()
		data["scope"] = scope

		if data:
			token = jwt.encode(data, private_key, algorithm='RS256')

			return token

		return None


	def get_json(self):
		"""
		Returns a json of all user data
		Currently it's just the username, but who knows what else it will hold in the future
		"""
		if self.id != None and self.username:
			return {
				"id": self.id,
				"username": self.username,
				"latitude": str(self.latitude),
				"longitude": str(self.longitude)
			}

		return None

	@property
	def username(self):
		return self._username


	@property
	def password(self):
		return self._password

	@property
	def latitude(self):
		return self._latitude
	
	@property
	def longitude(self):
		return self._longitude
	


	@property
	def password_hash(self):
		return self._password_hash

	@property
	def id(self):
		return self._id

	@property
	def scope(self):
		return self._scope
	
	

	""" Class methods """

	@classmethod
	def from_token(cls, token):
		claims = jwt.decode(token, DefaultConfig().get_public_key(), algorithms=['RS256'])

		if claims:
			print(claims)
			user = cls(id=claims.get("id"), username=claims.get("username"), scope=claims.get("scope"))
			return user

		return None