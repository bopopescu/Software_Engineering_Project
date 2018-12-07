import sys
import requests
import random
import json
import time

LOCAL_ADDRESS = "http://127.0.0.1:5000"
REMOTE_ADDRESS = "http://104.42.175.128"

LATITUDE = "38.951881"
LONGITUDE = "-92.333740"

USERNAME_BASE = "testdev"

FEED_API	= "/feed/v1"
MESSAGE_API = "/message/v1"
ACCOUNT_API = "/account/v1"

""" UNIT TESTS """

def test_create_account(address):
	address = address + ACCOUNT_API + "/create"

	username = USERNAME_BASE + str(random.randint(0,1000000))
	password = "password"

	request_body = {
		"username": username,
		"password": password,
		"first_name": "I'm",
		"last_name": "A Dev"
	}

	try:
		response = requests.post(address, json=request_body).json()
		print(response["message"])
	except Exception as error:
		print("Error executing test_create_account: {}".format(error))
		raise Exception(str(error))

	return request_body


def test_login_account(address, account):
	address = address + ACCOUNT_API + "/login"

	request_body = {
		"username": account["username"],
		"password": account["password"],
		"latitude": "38.792581",
		"longitude": "-92.495740"
	}

	try:
		response = requests.post(address, json=request_body).json()
		print(response["message"])
		print("Access token: {}...".format(response["token"][:100]))
	except Exception as error:
		print("Error executing test_login_account: {}".format(error))
		raise Exception(str(error))

	return response["token"]


def test_create_posts(address, token):
	address = address + FEED_API + "/create"

	headers = {
		"Authorization": "token {}".format(token)
	}

	for i in range(3):
		request_body = {
			"title": "Test title " + str(i),
			"body": "Test body " + str(i),
			"group_id": 0
		}

		try:
			response = requests.post(address, headers=headers, json=request_body).json()
			print(response["message"])
		except Exception as error:
			print("Error executing test_create_posts: {}".format(error))
			raise Exception(str(error))

	print("\n")


def test_fetch_posts(address, token):
	address = address + FEED_API + "/fetch"

	headers = {
		"Authorization": "token {}".format(token)
	}

	request_body = {
		"latitude": LATITUDE,
		"longitude": LONGITUDE,
		"group_id": 0
	}

	try:
		response = requests.post(address, headers=headers, json=request_body).json()
		print("Response recieved from server:")
		for post in response["posts"]:
			print(json.dumps(post, indent=4))
			time.sleep(1)
	except Exception as error:
		print("Error executing test_fetch_posts: {}".format(error))
		raise Exception(str(error))


def test_send_messages(address, token):
	address = address + MESSAGE_API + "/send"

	headers = {
		"Authorization": "token {}".format(token)
	}

	try:
		for i in range(1,5):
			request_body = {
				"to_id": i,
				"body": "Test body " + str(i)
			}

			response = requests.post(address, headers=headers, json=request_body)
			print(response)
	except Exception as error:
		print("Error executing test_send_messages: {}".format(error))
		raise Exception(str(error))


def test_fetch_messages(address, token):
	address = address + MESSAGE_API + "/fetch"

	headers = {
		"Authorization": "token {}".format(token)
	}

	try:
		for i in range(1,5):
			request_body = {
				"to_id": i
			}

			response = requests.post(address, headers=headers, json=request_body).json()
			print(json.dumps(response, indent=4))
	except Exception as error:
		print("Error executing test_fetch_messages: {}".format(error))
		raise Exception(str(error))
	

def test_add_friends(address, token, account):
	###
	print("Creating other user accounts to add friends")

	for i in range(3):
		request_body = {
			"username": account["username"] + "-testFriend" + str(i),
			"password": "password",
			"first_name": "I'm",
			"last_name": "aFriend"
		}

		response = requests.post(address + ACCOUNT_API + "/create", json=request_body).json()

		print(response["message"])

	address = address + ACCOUNT_API + "/friends/new"

	###

	headers = {
		"Authorization": "token {}".format(token)
	}

	try:
		for i in range(2, 5):
			request_body = {
				"friend_id": i
			}

			response = requests.post(address, headers=headers, json=request_body).json()
			print(response["message"])
	except Exception as error:
		print("Error executing test_add_friends: {}".format(error))
		raise Exception(str(error))


def test_fetch_friends(address, token):
	address = address + ACCOUNT_API + "/friends/fetch"

	headers = {
		"Authorization": "token {}".format(token)
	}

	try:
		response = requests.post(address, headers=headers, json={}).json()

		print("Location is updated when the user signs in so these may have null locations")
		for friend in response["friends"]:
			print(json.dumps(friend, indent=4))
	except Exception as error:
		print("Error executing test_fetch_friends: {}".format(error))
		raise Exception(str(error))

""" MAIN EXECUTION """

def run_unit_tests(address):
	try:
		print("Creating accounts for testing:")
		account = test_create_account(address)
		time.sleep(2)

		print("\n\nLogging in to account:")
		token = test_login_account(address, account)
		time.sleep(2)

		print("\n\nCreating posts:")
		test_create_posts(address, token)
		time.sleep(2)

		print("\n\nFetching nearby posts:")
		test_fetch_posts(address, token)
		time.sleep(2)

		print("\n\nSending messages:")
		test_send_messages(address, token)
		time.sleep(2)

		print("\n\nFetching sent messages:")
		test_fetch_messages(address, token)
		time.sleep(2)

		print("\n\nAdding friends:")
		test_add_friends(address, token, account)
		time.sleep(2)

		print("\n\nFetching friends:")
		test_fetch_friends(address, token)
		time.sleep(2)

	except Exception as error:
		print(error)
		return 1
	return 0


def main(argv):
	address = None

	if len(argv) < 2:
		error_message(argv)
	if argv[1] == "--local":
		address = LOCAL_ADDRESS
	elif argv[1] == "--remote":
		address = REMOTE_ADDRESS
	else:
		error_message(argv)

	rc = run_unit_tests(address)

	if rc != 0:
		print("Error occured while running unit tests: {}.\nPlease email nk529@mail.missouri.edu for assistance.".format(rc))
	else:
		print("Unit tests have been completed.\nPlease email nk529@mail.missouri.edu with any questions or concerns.\nThank you.")


def error_message(argv):
	print("Invalid command line arguments.\n{} <hosting>".format(argv[0]))
	print("Hosting choices are '--local' or '--remote'")
	sys.exit()

if __name__ == "__main__":
	main(sys.argv)