
class Post:
	def __init__(self, user, title, body):
		self._user = user
		self._title = title
		self._body = body

	@property
	def user(self):
		return self._user
	

	@property
	def title(self):
		return self._title

	@property
	def body(self):
		return self._body
	
	