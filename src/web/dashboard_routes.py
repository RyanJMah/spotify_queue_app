import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash

app_dashboard = flask.Blueprint("app_dashboard", __name__, template_folder = "templates")


@app_dashboard.route("/dashboard")
@flask_login.login_required
def dashboard():
    return flask.render_template("dashboard.html")

"""
@app_routes.route("/dashboard", methods = ["GET", "POST"])
@flask_login.login_required
def dashboard():
	if flask.request.method == "POST":
		handlers.upload_alarm_handler(flask.request.json)

	return flask.render_template("dashboard.html")
"""
