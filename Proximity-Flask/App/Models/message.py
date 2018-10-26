from App.Models import User

class Message:
	def __init__(self, user=None, to_id=None, body=None, time=None):
		self._user = user
		self._to_id = to_id
		self._body = body
		self._time = time


	def get_json(self):
		return {
			"from_id": self.user.id,
			"to_id": self.to_id,
			"body": self.body,
			"time": self.time
		}


	@property
	def user(self):
		return self._user

	@property
	def from_id(self):
		return self._user.id

	@property
	def to_id(self):
		return self._to_id
	
	@property
	def body(self):
		return self._body
	
	@property
	def time(self):
		return self._time
	
	@classmethod
	def from_list(cls, data):
		messages = []

		for datum in data:
			print(datum)
			messages.append(cls(user=User(id=datum[0]), to_id=datum[1], body=datum[2], time=datum[3]))

		return messages