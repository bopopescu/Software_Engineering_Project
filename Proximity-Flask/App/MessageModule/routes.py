from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	User,
	Message
)

from App import (
	database,
	config,
	authorization
)

message_api = Blueprint('MessageModule', __name__)

@message_api.route('/send')
@authorization.require_auth("AccountAccess")
def send_message(user):
	body = request.get_json()

	response = {}

	if body:
		message_body = body.get("body")
		message_to_id = body.get("to_id")

		if message_body and message_to_id:
			message = Message(from_id=user.id, to_id=message_to_id, body=message_body)
			database.send_message(message)

			response["message"] = "Sent {} to {}".format(message_body, message_to_id)

	return jsonify(response), 200


@message_api.route('/fetch')
@authorization.require_auth("AccountAccess")
def get_messages(user):
	body = request.get_json()

	response = {}

	if body:
		to_id = body.get("to_id")
		from_id = body.get("from_id")

		if to_id != None or from_id != None:
			messages = Message.from_list(database.get_messages(to_id, from_id))

			if messages:
				response["message"] = "Messages found."
				response["messages"] = []

				for message in messages:
					response["messages"].append(message.get_json())
			else:
				response["message"] = "Unable to find messages."

	return jsonify(response), 200