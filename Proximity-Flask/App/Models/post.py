from App.Models import _BaseModel

class Post(_BaseModel):
	def __init__(self, id=None, user_id=None, username=None, title=None, body=None, time=None, distance=None, latitude=None, longitude=None):
		self._user_id = user_id
		self._username = username
		self._title = title
		self._body = body
		self._time = time

		self._latitude = latitude
		self._longitude = longitude
		self._distance = distance


	def get_json(self):
		return {
			"id": self.id
			"user_id": self.user_id,
			"username": self.username,
			"title": self.title,
			"body": self.body,
			"time": self.time,
			"distance": self.distance
		}

	@property
	def id(self):
		return self._id	

	@property
	def user_id(self):
		return self._user_id

	@property
	def username(self):
		return self._username

	@property
	def title(self):
		return self._title

	@property
	def body(self):
		return self._body

	@property
	def time(self):
		return self._time
	
	@property
	def latitude(self):
		return self._latitude

	@property
	def longitude(self):
		return self._longitude

	@property
	def distance(self):
		return self._distance