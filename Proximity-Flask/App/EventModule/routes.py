from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	Event,
	Attendee
)

from App import (
	database,
	config,
	authorization
)

event_api = Blueprint('EventModule', __name__)


@event_api.route('/create', methods=['POST'])
@authorization.require_auth("AccountAccess")
def create_event(user):
	body = request.get_json()

	response = {}

	if body:
		owner = body.get("owner")
		title = body.get("title")
		latitude = body.get("latitude")
		longitude = body.get("longitude")

		if owner and title and latitude and longitude:
			event = Event(owner=owner, title=title, latitude=latitude, longitude=longitude)

			if database.create_event(event):
				response["message"] = "Event made"
			else:
				response["message"] = "Error making event."

	print(response, flush=True)

	return jsonify(response), 200


@event_api.route('/fetch', methods=['POST'])
@authorization.require_auth("AccountAccess")
def get_events(user):
	body = request.get_json()

	response = {}

	if body:
		latitude = body.get("latitude")
		longitude = body.get("longitude")


@event_api.route('/attendees/create', methods=['POST'])
@authorization.require_auth("AccountAccess")
def create_attendee(user):
	body = request.get_json()

	response = {}

	if body:
		event_id = body.get("event_id")

		if event_id:
			attendee = Attendee(event_id=event_id, user_id=user.id)

			if database.create_attendee(attendee):
				response["message"] = "Attendee made"
			else:
				response["message"] = "Error making attendee."

	print(response, flush=True)

	return jsonify(response), 200


@event_api.route('/attendees/fetch', methods=['POST'])
@authorization.require_auth("AccountAccess")
def get_attendees(user):
	body = request.get_json()

	response = {}

	if body:
		event_id = body.get("event_id")

		if event_id:
			attendees = Attendee.from_list(database.get_attendees(event_id))

			if attendees:
				response = []

				for attendee in attendees:
					response.append(attendee.get_json())
			else:
				response["message"] = "Unable to fetch attendees"

	print(response, flush=True)

	return jsonify(response), 200
