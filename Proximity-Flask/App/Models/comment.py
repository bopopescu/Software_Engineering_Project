from App.Models import _BaseModel

class Comment(_BaseModel):
	def __init__(self, id=None, user_id=None, post_id=None, time=None, body=None):
		self._id = id
		self._user_id = user_id
		self._post_id = post_id
		self._time = time
		self._body = body

	def get_json(self):
		return {
			"id": self.id,
			"user": self.user_id,
			"post_id": self.post_id,
			"body": self.body,
			"time": self.time
		}

	@property
	def id(self):
		return self._id
	
	@property
	def user_id(self):
		return self._user_id

	@property
	def post_id(self):
		return self._post_id
	
	@property
	def time(self):
		return self._time
	
	@property
	def body(self):
		return self._body
	