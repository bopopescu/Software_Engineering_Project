import mysql.connector
from flask import Flask

from App.Models import (
	DefaultConfig,
	DatabaseController
)

""" Objects for backend """
config = DefaultConfig()

db_conn = mysql.connector.connect(
	host=config.host,
	user=config.user,
	passwd=config.password
)

database = DatabaseController(db_conn, config)

""" Backend APIs """
from App.AccountModule import account_api

""" Gunicorn entry point """
app = Flask(__name__)

# supported APIs
app.register_blueprint(account_api, url_prefix="/account/v1")

""" Test route """
@app.route('/')
def test():
	return "Ok", 200