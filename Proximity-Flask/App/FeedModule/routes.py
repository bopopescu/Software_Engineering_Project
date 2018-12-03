from flask import (
	Blueprint, 
	request,
	jsonify
)

from App.Models import (
	User,
	Post,
	Comment
)

from App import (
	database,
	config,
	authorization
)

feed_api = Blueprint('FeedModule', __name__)

@feed_api.route('/create', methods=['POST'])
@authorization.require_auth("AccountAccess")
def create_post(user):
	print("Creating post for: ", user.id)
	body = request.get_json()

	response = {}

	if body:
		post_title = body.get("title")
		post_body = body.get("body")
		post_latitude = body.get("latitude")
		post_longitude = body.get("longitude")

		if post_title and post_body and post_latitude and post_longitude:
			post = Post(user_id=user.id, title=post_title, body=post_body, latitude=post_latitude, longitude=post_longitude)

			if database.create_post(post):
				response["message"] = "User {} made a post with title '{}' and body '{}'.".format(user.username, post.title, post.body)
			else:
				response["message"] = "Error making post."
		else:
			response["message"] = "Post title and post body must be present."

	return jsonify(response), 200


@feed_api.route('/fetch', methods=['POST'])
@authorization.require_auth("AccountAccess")
def get_posts(user):
	body = request.get_json()

	print(body, flush=True)

	response = {}

	if body:
		latitude = body.get("latitude")
		longitude = body.get("longitude")
		group_id = body.get("group_id", 0)

		# print(request.args, flush=True)
		# print(request.query_string, flush=True)

		# latitude = request.args.get("latitude")
		# longitude = request.args.get("longitude")
		# group_id = request.args.get("group_id", 0)

		print("{} {}".format(latitude, longitude), flush=True)

		if latitude and longitude:
			posts = Post.from_list(database.get_posts(latitude, longitude, 100, group_id=group_id))

			print(posts, flush=True)

			if posts:
				response["posts"] = []

				for post in posts:
					response["posts"].append(post.get_json())
			else:
				response["message"] = "Unable to find posts."

	print(response, flush=True)

	return jsonify(response), 200


@feed_api.route('/delete', methods=['POST'])
@authorization.require_auth("AccountAccess")
def delete_post(user):
	body = request.get_json()

	response = {}

	if body:
		post_id = body.get("id")

		if post_id:
			if database.delete_post(post_id):
				response["message"] = "Post {} deleted.".format(post_id)
			else:
				response["message"] = "Unable to delete post."

	return jsonify(response), 200


@feed_api.route('/comments/fetch')
@authorization.require_auth("AccountAccess")
def get_comments(user):
	body = request.get_json()

	response = {}

	if body:
		post_id = body.get("post_id")

		if post_id:
			comments = Comment.from_list(database.get_comments(post_id = post_id))

			print(comments, flush=True)

			if comments:
				response = []

				for comment in comments:
					response.append(comment.get_json())
			else:
				response["message"] = "Unable to find comments."

	print(response, flush=True)

	return jsonify(response), 200


@feed_api.route('/comments/create', methods=['POST'])
@authorization.require_auth("AccountAccess")
def create_comment(user):
	body = request.get_json()

	response = {}

	if body:
		post_id = body.get("post_id")
		comment_body = body.get("body")

		comment = Comment(user_id = user.id, post_id = post_id, body=comment_body)

		if database.create_comment(comment):
			response["message"] = "Created comment"

	return jsonify(response), 200