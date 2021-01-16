import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash

app_routes = flask.Blueprint("app_routes", __name__, template_folder = "templates")


@app_routes.route("/")
def index():
	return flask.render_template("dashboard.html")
	# if is_logged_in():
	# 	return flask.redirect(flask.url_for("app_routes.dashboard"))
	# else:
	# 	return flask.redirect(flask.url_for("app_routes.login"))


@app_routes.route("/dashboard", methods = ["GET", "POST"])
@flask_login.login_required
def dashboard():
	if flask.request.method == "POST":
		handlers.upload_alarm_handler(flask.request.json)

	return flask.render_template("dashboard.html")



