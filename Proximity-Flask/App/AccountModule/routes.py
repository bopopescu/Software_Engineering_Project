from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	User,
	Friendship
)

from App import (
	database,
	config,
	authorization
)

account_api = Blueprint('AccountModule', __name__)

@account_api.route('/create', methods=['POST'])
def account_create():
	body = request.get_json()

	response = {}

	if body:
		username = body.get('username')
		password = body.get('password')

		if username and password:
			user = User(username=username, password=password)

			if database.create_user(user):
				response["message"] = "Account {} created!".format(username)
			else:
				response["message"] = "Error creating account {}.".format(username)

	return jsonify(response), 200


@account_api.route('/login')
def account_login():
	body = request.get_json()

	response = {}

	if body:
		username = body.get('username')
		password = body.get('password')
		user_latitude = body.get('latitude')
		user_longitude = body.get('longitude')

		if username and password:
			user = User(username=username, password=password)

			if database.verify_user(user):
				token = user.get_token("AccountAccess")

				if user_latitude and user_longitude:
					database.update_user_location(user.id, user_latitude, user_longitude)

				if token:
					response["token"] = token.decode('utf8')
					response["message"] = "Account {} logged in!".format(username)
				else:
					response["message"] = "Error logging in with {}.".format(username)
			else:
				response["message"] = "Unable to login with account {}.".format(username)

	return jsonify(response), 200


@account_api.route('/reset', methods=['POST'])
def password_reset():
	body = request.get_json()

	response = {}

	if body:
		username = body.get('username')
		old_password = body.get('old_password')
		new_password = body.get('new_password')

		if username and old_password and new_password:
			user = User(username=username, password=old_password)

			if database.verify_user(user):
				if database.update_user(user, password=new_password):
					response["message"] = "Password for {} has been changed.".format(username)
				else:
					response["message"] = "Error changing password for {}.".format(username)
			else:
				response["message"] = "Unable to verify user {} with that password".format(old_password)

	return jsonify(response), 200


@account_api.route('/friends/new', methods=['POST'])
@authorization.require_auth("AccountAccess")
def new_friend(user):
	body = request.get_json()

	response = {}

	if body:
		friend_id = body.get('friend_id')

		if friend_id != None:
			friendship = Friendship(user.id, friend_id)

			if database.new_friendship(friendship):
				response["message"] = "Friendship between {} and {} added".format(user.id, friend_id)
			else:
				response["message"] = "Error adding friendship between {} and {}".format(user.id, friend_id)

	return jsonify(response), 200


@account_api.route('friends/fetch')
@authorization.require_auth("AccountAccess")
def get_friends(user):
	body = request.get_json()

	response = {}

	if body:
		friends = User.from_list(database.get_friends(user.id))

		if friends:
			response["message"] = "Friends found."
			response["friends"] = []

			for friend in friends:
				response["friends"].append(friend.get_json())
		else:
			response["message"] = "Unable to find friends."

	return jsonify(response), 200