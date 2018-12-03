from flask import (
	Blueprint, 
	request,
	jsonify,
	abort
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


@account_api.route('/profile/<int:user_id>', methods=['POST'])
def profile(user_id):
	user_data = database.get_user(user_id)

	if user_data:
		user = User.from_row(user_data)
		response = user.get_json()
		return jsonify(response), 200

	return abort(404)


@account_api.route('/create', methods=['POST'])
def account_create():
	body = request.get_json()

	response = {}

	if body:
		username = body.get('username')
		password = body.get('password')
		first_name = body.get('first_name')
		last_name = body.get('last_name')

		if username and password and first_name and last_name:
			user = User(username=username, password=password, first_name=first_name, last_name=last_name)

			if database.create_user(user):
				response["message"] = "Account {} created!".format(username)
			else:
				response["message"] = "Error creating account {}.".format(username)

	return jsonify(response), 200


@account_api.route('/login', methods=['POST'])
def account_login():
	body = request.get_json()

	print(str(body), flush=True)

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
					response["user"] = user.get_json()
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


@account_api.route('friends/fetch', methods=['POST'])
@authorization.require_auth("AccountAccess")
def get_friends(user):
	body = request.get_json()

	response = {}

	if body:
		# latitude = body.get("latitude")
		# longitude = body.get("longitude")

		latitude = user.latitude
		longitude = user.longitude

		print("{} {}".format(latitude, longitude))

		if latitude and longitude:
			friends = User.from_list(database.get_friends(user.id, latitude, longitude))

			if friends:
				response = []

				for friend in friends:
					response.append(friend.get_json())
			else:
				response["message"] = "Unable to find friends."

	return jsonify(response), 200
