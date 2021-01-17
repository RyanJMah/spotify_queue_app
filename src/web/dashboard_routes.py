import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash
from sql import delete_queue

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
