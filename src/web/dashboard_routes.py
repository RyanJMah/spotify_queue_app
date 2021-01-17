import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash

app_dashboard = flask.Blueprint("app_dashboard", __name__, template_folder = "templates")

@app_dashboard.route("/join-or-host")
def join_or_host():
	if "toke" in flask.session.keys():
		return flask.render_template("join_or_host.html", page_name = "Host")
	else:
		return flask.abort(403)

@app_dashboard.route("/dashboard/host")
def dashboard_host():
	if "toke" in flask.session.keys():
		songs = [
			{"name": "WAP", "artist": "Cardi B"},
			{"name": "asdfasdf", "artist": "Ryan Mah"}
		]

		return flask.render_template("host_dashboard.html", page_name = "Host", songs = songs)
	else:
		return flask.abort(403)

