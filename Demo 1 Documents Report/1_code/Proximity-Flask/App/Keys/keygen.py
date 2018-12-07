from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import load_pem_private_key

import jwt

""" RSA """

key_pair = rsa.generate_private_key(
	public_exponent = 65537,
	key_size = 2048,
	backend = default_backend()
)

public_key = key_pair.public_key()

public_pem = public_key.public_bytes(
	encoding = serialization.Encoding.PEM,
	format = serialization.PublicFormat.SubjectPublicKeyInfo
)

private_pem = key_pair.private_bytes(
	encoding = serialization.Encoding.PEM,
	format = serialization.PrivateFormat.PKCS8,
	encryption_algorithm = serialization.BestAvailableEncryption(b'4320Group16')
)

# with open("public_key.pem", "w") as key_file:
# 	key_file.write(public_pem.decode('utf8'))

# with open("private_key.pem", "w") as key_file:
# 	key_file.write(private_pem.decode('utf8'))

private_key = load_pem_private_key(private_pem, password=b"4320Group16", backend=default_backend())
encoded = jwt.encode({'some': 'payload'}, private_key, algorithm='RS256')
print(encoded)

decoded = jwt.decode(encoded, public_pem, algorithms='RS256')
print(decoded)