import os
import sys
import flask
import flask_login
import flask_cors
import requests

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(os.path.join(PARENT_DIR, "API"))

from dashboard_routes import app_dashboard
import auth

app_login = flask.Blueprint("app_login", __name__, template_folder = "templates")

# @app_login.route("/test")
# def test():
# 	return flask.session["toke"]

@app_login.route("/")
def index():
	return flask.redirect(flask.url_for("app_login.login"))


@app_login.route("/login", methods = ["POST", "GET"])
def login():
	if flask.request.method == "POST":
		print(flask.request.form)
		auth_url = auth.get_auth_url()
		return auth_url
	
	else:
		return flask.render_template("login.html")

@app_login.route("/spotify_token_callback")
def spotify_token_callback():
	flask.session.clear()
	
	code = flask.request.args.get('code')
	res = auth.get_auth_token(code)
	flask.session["toke"] = res.json().get("access_token")

	print(flask.session["toke"])
	return flask.redirect(flask.url_for("app_dashboard.join_or_host"))




