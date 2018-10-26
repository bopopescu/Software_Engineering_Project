from App.Models import User

class Post:
	def __init__(self, user=None, title=None, body=None, time=None, latitude=None, longitude=None, distance=None):
		self._user = user
		self._title = title
		self._body = body
		self._time = time

		self._latitude = latitude
		self._longitude = longitude
		self._distance = distance


	def get_json(self):
		return {
			"user_id": self.user.id,
			"title": self.title,
			"body": self.body,
			"time": self.time,
			"distance": self.distance
		}


	@property
	def user(self):
		return self._user

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
	
	

	""" Class Methods """

	@classmethod
	def from_list(cls, data):
		posts = []

		for datum in data:
			posts.append(cls(user=User(id=datum[0]), title=datum[1], body=datum[2], time=datum[3], distance=datum[4]))

		return posts