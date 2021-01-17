import os
import flask
import flask_login
# import handlers
from werkzeug.security import generate_password_hash, check_password_hash
from flask_mysqldb import MySQL

app_dashboard = flask.Blueprint("app_dashboard", __name__, template_folder = "templates")

app_dashboard.config['MYSQL_USER'] = ''
app_dashboard.config['MYSQL_PASSWORD'] = ''
app_dashboard.config['MYSQL_HOST'] = ''
app_dashboard.config['MYSQL_DB'] = ''
app_dashboard.config['MYSQL_CURSORCLASS'] = ''
mysql = MySQL(app_dashboard)

@app_dashboard.route("/dashboard", methods = ["GET", "POST", "DELETE"])
def dashboard():
    if flask.request.method == "POST":
        print(flask.request.json)
    
    elif flask.request.method == "DELETE":  # Deleting a song from the queue located in the nono table in the database
        cur = mysql.connection.cursor()
        cur.execute('''DELETE FROM  ''')

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
