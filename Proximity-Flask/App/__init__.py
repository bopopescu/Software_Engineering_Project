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

""" Backend APIs """
from App.AccountModule import account_api

""" Gunicorn entry point """
app = Flask(__name__)

# supported APIs
app.register_blueprint(account_api, url_prefix="/account/v1")
print("Account API active")

""" Test route """
@app.route('/test')
def test():
	return "Ok", 200

print("Launched")