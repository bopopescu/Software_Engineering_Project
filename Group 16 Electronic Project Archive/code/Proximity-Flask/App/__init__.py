# Written by: Nathan Kulczak

import MySQLdb
from flask import Flask

from App.Models import (
	DefaultConfig,
	DatabaseController
)

print("Launching...")



""" Objects for backend """
config = DefaultConfig()
print("Config used: {}".format(config))

# db_conn = MySQLdb.connect(
# 	host=config.host,
# 	user=config.user,
# 	passwd=config.password,
# 	db=config.database
# )
# print("Connected to database: {}".format(db_conn))

database = DatabaseController(None, config)
print("Database controller used: {}".format(DatabaseController))



""" Authorization Provider """

from App.Models import DefaultAuthorization

authorization = DefaultAuthorization(config=config)
print("Authorization used: {}".format(authorization))



""" Gunicorn entry point """
app = Flask(__name__)



""" Backend APIs """
from App.AccountModule import account_api
from App.FeedModule import feed_api
from App.MessageModule import message_api
from App.GroupModule import group_api
from App.EventModule import event_api

app.register_blueprint(account_api, url_prefix="/account/v1")
print("Account API active")
app.register_blueprint(feed_api, url_prefix="/feed/v1")
print("Feed API active")
app.register_blueprint(message_api, url_prefix="/message/v1")
print("Message API active")
app.register_blueprint(group_api, url_prefix="/group/v1")
print("Group API active")
app.register_blueprint(event_api, url_prefix="/event/v1")
print("Event API active")


""" Test route """
@app.route('/test')
def test():
	return "Ok", 200

print("Launched")