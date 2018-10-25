from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	User,
	Post
)

from App import (
	database,
	config,
	authorization
)

feed_api = Blueprint('FeedModule', __name__)

@feed_api.route('/create')
@authorization.require_auth("AccountAccess")
def create_post(user):
	body = request.get_json()

	response = {}

	if body:
		post_title = body.get("title")
		post_body = body.get("body")
		post_latitude = body.get("latitude")
		post_longitude = body.get("longitude")

		if post_title and post_body and post_latitude and post_longitude:
			post = Post(user=user, title=post_title, body=post_body, latitude=post_latitude, longitude=post_longitude)

			if database.create_post(post):
				response["message"] = "User {} made a post with title '{}' and body '{}'.".format(user.username, post.title, post.body)
			else:
				response["message"] = "Error making post."
		else:
			response["message"] = "Post title and post body must be present."

	return jsonify(response), 200


@feed_api.route('/fetch')
@authorization.require_auth("AccountAccess")
def get_posts(user):
	body = request.get_json()

	response = {}

	if body:
		latitude = body.get("latitude")
		longitude = body.get("longitude")

		if latitude and longitude:
			posts = Post.from_list(database.get_posts(latitude, longitude, 100))

			if posts:
				response["message"] = "Posts found."
				response["posts"] = []
				for post in posts:
					response["posts"].append(post.get_json())
			else:
				response["message"] = "Unable to find posts."

	return jsonify(response), 200