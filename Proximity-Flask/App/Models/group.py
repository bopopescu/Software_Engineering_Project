
class Group:
	def __init__(self, id=None, name=None, private=None):
		self._id = id
		self._name = name
		self._private = private


	@property
	def id(self):
		return self._id

	@property
	def name(self):
		return self._name

	@property
	def private(self):
		return self._private
	