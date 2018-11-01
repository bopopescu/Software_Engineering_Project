from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key

class DefaultConfig:
	""" Database Connection Info """
	host = "proximitydatabase.cbcqll27hw91.us-west-2.rds.amazonaws.com"
	user = "admin"
	password = "4320Group16"
	database = "proximity_database"

	""" Databse Config Info """
	user_table = "[User]"
	post_table = "Post"
	message_table = "Message"
	group_table = "[Group]"
	friendship_table = "Friendship"

	""" Security Info """
	
	private_key_filepath = "/home/developer/Software_Engineering_Project/Proximity-Flask/App/Keys/private_key.pem"
	public_key_filepath = "/home/developer/Software_Engineering_Project/Proximity-Flask/App/Keys/public_key.pem"

	private_key_password = b"4320Group16"


	@classmethod
	def get_private_key(cls):
		key = None
		with open(cls.private_key_filepath) as file:
			encrypted_key = file.read().encode()

			key = load_pem_private_key(encrypted_key, password=cls.private_key_password, backend=default_backend())

		return key


	@classmethod
	def get_public_key(cls):
		key = None
		with open(cls.public_key_filepath) as file:
			key = file.read().encode()

		return key

	def __str__(self):
		return "Default Config"
