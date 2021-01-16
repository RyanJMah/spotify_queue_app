import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash

app_login = flask.Blueprint("app_login", __name__, template_folder = "templates")
