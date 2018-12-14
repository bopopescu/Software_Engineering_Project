# Written by: Nathan Kulczak

from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	Group,
	Message
)

from App import (
	database,
	config,
	authorization
)


group_api = Blueprint('GroupModule', __name__)


@group_api.route('/fetch', methods=['POST'])
@authorization.require_auth("AccountAccess")
def get_groups(user):
	body = request.get_json()

	response = {}

	if body:
		latitude = body.get("latitude")
		longitude = body.get("longitude")

		if latitude and longitude:
			groups = Group.from_list(database.get_groups(latitude, longitude))

			print(groups, flush=True)

			if groups:
				response = []

				for group in groups:
					response.append(group.get_json())
			else:
				response["message"] = "Unable to find groups."

	print(response, flush=True)

	return jsonify(response), 200


@group_api.route('/create', methods=['POST'])
@authorization.require_auth("AccountAccess")
def create_group(user):
	body = request.get_json()

	response = {}

	if body:
		latitude = body.get("latitude")
		longitude = body.get("longitude")
		name = body.get("name")
		private = body.get("private", False)

		if latitude and longitude and name:

			group = Group(owner=user.id, name=name, private=private, latitude=latitude, longitude=longitude)

			if database.create_group(group):
				response["message"] = "User {} made a group with name '{}.".format(user.username, group.name)
			else:
				response["message"] = "Error making group."
		else:
			response["message"] = "Latitude, longitude, and group name must be present."

	print(response, flush=True)

	return jsonify(response), 200


@group_api.route('/delete', methods=['POST'])
def delete_group(user):
	body = request.get_json()

	response = {}

	if body:
		group = body.get("group")

		if group:
			database.delete_group(group)
			response["message"] = "Group {} deleted.".format(group)

	print(response, flush=True)

	return jsonify(response), 200



@group_api.route('/invite', methods=['POST'])
@authorization.require_auth("AccountAccess")
def create_group_invite(user):
	body = request.get_json()

	response = {}

	if body:
		recipient = body.get("recipient")
		group_id = body.get("group")

		if recipient:
			group = Group.from_row(database.get_group(group_id))

			message = Message(from_id=user.id, to_id=recipient, body="{} has invited you to join {}".format(user.username, group.name))
			database.send_message(message)

			response["message"] = "Sent {} to {}".format(message.body, message.to_id)

	return jsonify(response), 200
