import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash

app_login = flask.Blueprint("app_login", __name__, template_folder = "templates")


@app_login.route("/")
def index():
	return flask.redirect(flask.url_for("app_login.login"))
	# if is_logged_in():
	# 	return flask.redirect(flask.url_for("app_routes.dashboard"))
	# else:
	# 	return flask.redirect(flask.url_for("app_routes.login"))

@app_login.route("/login", methods = ["POST", "GET"])
def login():
	if flask.request.method == "POST":
		print(flask.request.json)
		print(type(flask.request.json))

	return flask.render_template("login.html")

if __name__ == "__main__":
	login()

# @app_routes.route("/host/dashboard", methods = ["GET", "POST"])
# @flask_login.login_required
# def dashboard():
# 	if flask.request.method == "POST":
# 		handlers.upload_alarm_handler(flask.request.json)

# 	return flask.render_template("dashboard.html")



