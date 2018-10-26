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

db_conn = MySQLdb.connect(
	host=config.host,
	user=config.user,
	passwd=config.password,
	db=config.database
)
print("Connected to database: {}".format(db_conn))

database = DatabaseController(db_conn, config)
print("Database controller used: {}".format(DatabaseController))



""" Authorization Provider """

from App.AccountModule import DefaultAuthorization

authorization = DefaultAuthorization(config=config)
print("Authorization used: {}".format(authorization))



""" Gunicorn entry point """
app = Flask(__name__)



""" Backend APIs """
from App.AccountModule import account_api
from App.FeedModule import feed_api
from App.MessageModule import message_api

app.register_blueprint(account_api, url_prefix="/account/v1")
print("Account API active")
app.register_blueprint(feed_api, url_prefix="/feed/v1")
print("Feed API active")
app.register_blueprint(message_api, url_prefix="/message/v1")
print("Message API active")



""" Test route """
@app.route('/test')
def test():
	return "Ok", 200

print("Launched")