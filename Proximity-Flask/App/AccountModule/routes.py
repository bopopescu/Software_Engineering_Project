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
			user = User(username, password)

			if database.create_user(user):
				response["message"] = "Account {} created!".format(username)
			else:
				response["message"] = "Error creating account {}.".format(username)

	return jsonify(response), 200


@account_api.route('/login')
def account_login():
	pass