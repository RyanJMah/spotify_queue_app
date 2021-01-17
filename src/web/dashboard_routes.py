import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash
from sql import delete_queue

<<<<<<< HEAD
@app_dashboard.route("/dashboard", methods = ["GET", "POST", "DELETE"])
def dashboard():
    if flask.request.method == "POST":
        print(flask.request.json)
    
    elif flask.request.method == "DELETE":  # Deleting a song from the queue located in the nono table in the database
        

    else:  #GET
        queue = flask.request.args.get('????')  # updated queue in the dashboard from the webserver
        return render_template("dashboard.html", queue=queue )

    return flask.render_template("dashboard.html")





"""
@app_routes.route("/dashboard", methods = ["GET", "POST"])
@flask_login.login_required
def dashboard():
	if flask.request.method == "POST":
		handlers.upload_alarm_handler(flask.request.json)

	return flask.render_template("dashboard.html")
"""
=======
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

>>>>>>> 9bccb939993f780992440cd78c2da8307e0b7ca7
