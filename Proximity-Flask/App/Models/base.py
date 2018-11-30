
class _BaseModel:
	"""
	Base model class
	"""

	def fill_in_user(self, item):
		user = self._database.get_user(datum.get("user_id"))

		datum["username"] = user[1]
		# and whatever else we want to add

	@classmethod
	def from_row(cls, datum):
		return cls(*datum)

	@classmethod
	def from_list(cls, data):
		models = []

		for datum in data:
			models.append(cls(*datum))

		return models
