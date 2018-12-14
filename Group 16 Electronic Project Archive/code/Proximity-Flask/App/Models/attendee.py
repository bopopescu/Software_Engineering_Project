# Written by: Nathan Kulczak

from App.Models import _BaseModel

class Attendee(_BaseModel):
	def __init__(self, id=None, event_id=None, user_id=None):
		self._id = id
		self._event_id = event_id
		self._user_id = user_id

	def get_json(self):
		return {
			"id": self.id,
			"event_id": self.event_id,
			"user_id": self.user_id
		}


	@property
	def id(self):
		return self._id
	
	@property
	def event_id(self):
		return self._event_id
	
	@property
	def user_id(self):
		return self._user_id
	