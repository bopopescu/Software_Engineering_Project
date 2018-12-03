from App.Models import _BaseModel

class Event(_BaseModel):
	def __init__(self, id=None, owner=None, title=None, latitude=None, longitude=None, time=None, distance=None):
		self._id = id
		self._owner = owner
		self._title = title
		self._latitude = latitude
		self._longitude = longitude
		self._time = time
		self._distance = distance

	def get_json(self):
		return {
			"id": self.id,
			"owner": self.owner,
			"title": self.title,
			"latitude": str(self.latitude),
			"longitude": str(self.longitude),
			"time": self.time.strftime("%Y-%m-%d %H:%M:%S"),
			"distance": str(self.distance)
		}

	@property
	def id(self):
		return self._id
	
	@property
	def owner(self):
		return self._owner
	
	@property
	def title(self):
		return self._title
	
	@property
	def latitude(self):
		return self._latitude
	
	@property
	def longitude(self):
		return self._longitude
	
	@property
	def time(self):
		return self._time
	
	@property
	def distance(self):
		return self._distance
	