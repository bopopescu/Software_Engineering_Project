# Written by: Nathan Kulczak

from App.Models import _BaseModel

class Message(_BaseModel):
	def __init__(self, from_id=None, to_id=None, body=None, time=None):
		self._from_id = from_id
		self._to_id = to_id
		self._body = body
		self._time = time


	def get_json(self):
		return {
			"from_id": self.from_id,
			"to_id": self.to_id,
			"body": self.body,
			"time": self.time
		}

	@property
	def from_id(self):
		return self._from_id

	@property
	def to_id(self):
		return self._to_id
	
	@property
	def body(self):
		return self._body
	
	@property
	def time(self):
		return self._time
