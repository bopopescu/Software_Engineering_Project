from App.Models import _BaseModel

class Friendship(_BaseModel):
	def __init__(self, user_one, user_two):
		self._user_one = user_one
		self._user_two = user_two

	@property
	def user_one(self):
		return self._user_one

	@property
	def user_two(self):
		return self._user_two