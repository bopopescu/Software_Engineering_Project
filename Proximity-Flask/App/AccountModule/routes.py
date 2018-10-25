from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	User
)

from App import (
	database,
	config
)

account_api = Blueprint('AccountModule', __name__)

@account_api.route('/create')
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

		if username and password:
			user = User(username=username, password=password)

			if database.verify_user(user):
				token = user.get_token("AccountAccess")

				if token:
					response["token"] = token.decode('utf8')
					response["message"] = "Account {} logged in!".format(username)
				else:
					response["message"] = "Error logging in with {}.".format(username)
			else:
				response["message"] = "Unable to login with account {}.".format(username)

	return jsonify(response), 200


@account_api.route('/reset')
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