# Written by: Nathan Kulczak

from App.Models import _BaseModel

class Group(_BaseModel):
	def __init__(self, id=None, owner=None, name=None, private=None, latitude=None, longitude=None, distance=None):
		self._id = id
		self._owner = owner
		self._name = name
		self._private = private
		self._latitude = latitude
		self._longitude = longitude
		self._distance = distance

	def get_json(self):
		return {
			"owner": self.owner,
			"name": self.name,
			"private": self.private,
			"latitude": str(self.latitude),
			"longitude": str(self.longitude),
			"distance": self.distance
		}

	@property
	def name(self):
		return self._name

	@property
	def owner(self):
		return self._owner
	

	@property
	def private(self):
		return self._private

	@property
	def latitude(self):
		return self._latitude

	@property
	def longitude(self):
		return self._longitude

	@property
	def id(self):
		return self._id

	@property
	def distance(self):
		return self._distance
	
	
	
	