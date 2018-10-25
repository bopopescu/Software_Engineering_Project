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

@feed_api.route('/post')
@authorization.require_auth("AccountAccess")
def create_post(user):
	body = request.get_json()

	response = {}

	if body:
		post_title = body.get("title")
		post_body = body.get("body")

		if post_title and post_body:
			post = Post(title=post_title, body=post_body)

			if database.create_post(post):
				response["message"] = "User {} made a post with title '{}' and body '{}'.".format(user.username, post.title, post.body)
			else:
				response["message"] = "Error making post."
		else:
			response["message"] = "Post title and post body must be present."

	return response