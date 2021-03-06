import os
import sys
import flask
import datetime

from login_routes import app_login
from dashboard_routes import app_dashboard

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)

from credentials import *

# TIMEOUT_MINUTES = 2

def app_init(app):
	app.secret_key = APP_SECRET_KEY
	app.register_blueprint(app_login)
	app.register_blueprint(app_dashboard)

	# @app.before_request
	# def make_session_permanent():
	# 	flask.session.permanent = True
	# 	app.permanent_session_lifetime = datetime.timedelta(minutes = TIMEOUT_MINUTES)

	# login_manager = flask_login.LoginManager()
	# login_manager.init_app(app)
	# @login_manager.user_loader
	# def load_user(user_id):
	# 	return user.get_user_from_id(user_id)


app = flask.Flask(__name__)
app_init(app)


