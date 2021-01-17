import os
import sys
import flask
import flask_login
import numpy as np
from datetime import datetime
# import handlers

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(os.path.join(PARENT_DIR, "SQL"))
sys.path.append(os.path.join(PARENT_DIR, "API"))

import sql
import spotify_api

app_dashboard = flask.Blueprint("app_dashboard", __name__, template_folder = "templates")

def compare_songs(song1, song2):
	return (song1["name"] == song2["name"]) and (song1["artist"] == song2["artist"])

def generate_session_id():
	def append_zeros(string):
		while len(string) < 4:
			string = "0" + string
		return string

	df = sql.read_session()
	curr_max = np.max([int(sess_id) for sess_id in df["session_id"].to_list()])
	new_sess_id = append_zeros(str(curr_max + 1))

	sql.add_session(new_sess_id, flask.session["toke"])
	flask.session["session_id"] = new_sess_id

################################################################################################
# GENERAL ROUTES
@app_dashboard.route("/join-or-host")
def join_or_host():
	if "toke" in flask.session.keys():
		return flask.render_template("join_or_host.html", page_name = "Host")
	else:
		return flask.abort(403)

@app_dashboard.route("/guest-enter-session-id", methods = ["POST", "GET"])
def guest_enter_session_id():
	if flask.request.method == "POST":
		# print(dict(flask.request.form))
		flask.session["session_id"] = flask.request.form["session_id"]
		return flask.redirect(flask.url_for("app_dashboard.dashboard_guest"))

	return flask.render_template("guest_enter_id.html")
################################################################################################

################################################################################################
# HOST ROUTES
def dashboard_host_post_handler(params):
	# print(params)
	if params["command"] == "queue_song":
		target_song = [song for song in flask.session["requested_songs"] if compare_songs(song, params)][0]
		
		spotify_api.add_to_playlist(flask.session["toke"], flask.session["playlist_id"], [target_song["song_id"],])
		spotify_api.add_to_queue(flask.session["toke"], target_song["song_id"])


		temp = flask.session["requested_songs"]	
		temp = [song for song in temp if not compare_songs(song, params)]
		flask.session["requested_songs"] = temp

	elif params["command"] == "remove_song":
		temp = flask.session["requested_songs"]	
		temp = [song for song in temp if not compare_songs(song, params)]
		flask.session["requested_songs"] = temp


@app_dashboard.route("/dashboard-host", methods = ["POST", "GET"])
def dashboard_host():
	if flask.request.method == "POST":
		response = dashboard_host_post_handler(flask.request.json)
		if response is not None:
			return response

	if "toke" in flask.session.keys():
		if "session_id" not in flask.session.keys():
			generate_session_id()

		if "requested_songs" not in flask.session.keys():
			flask.session["requested_songs"] = []

		if "playlist_id" not in flask.session.keys():
			flask.session["playlist_id"] = spotify_api.create_playlist(flask.session["toke"])

		df = sql.read_queue(session_id = flask.session["session_id"])
		sql.delete_queue(session_id = flask.session["session_id"])
		requested_songs = []
		for row in df.to_dict(orient = "records"):
			temp = spotify_api.get_song_info_by_id(flask.session["toke"], row["song_id"])
			temp["requested_by"] = row["guest_user"]
			temp["song_id"] = row["song_id"]
			requested_songs.append(temp)

		if requested_songs != []:
			flask.session["requested_songs"] += requested_songs

		curr_song = spotify_api.current_song_info(flask.session["toke"])
		queued_songs = [
			{"name": "WAP", "artist": "Cardi B"},
			{"name": "asdfasdf", "artist": "Ryan Mah"}
		]
		# requested_songs = [
		# 	{"name": "WAP", "artist": "Cardi B", "requested_by": "Ryan Mah"}
		# ]
		
		# print("asdfasdf")
		# print(flask.session["queue"])
		# print(flask.session["requested_songs"])
		return flask.render_template(
			"host_dashboard.html",
			session_id = flask.session["session_id"],
			page_name = "Host",
			current_song = curr_song,
			queued_songs = queued_songs,
			# queue_song = spotify_api.get_playlist_queue(flask.session["toke"], flask.session["playlist_id"], curr_song["song_id"]),
			requested_songs = flask.session["requested_songs"]
		)
	else:
		return flask.abort(403)

################################################################################################

################################################################################################
# GUEST ROUTES
@app_dashboard.route("/dashboard-guest", methods = ["POST", "GET"])
def dashboard_guest():
	if flask.request.method == "POST":
		flask.session["searched_song"] = flask.request.form["song"]
		return flask.redirect(flask.url_for("app_dashboard.search_song"))

	if "toke" in flask.session.keys():
		token = sql.read_session(flask.session["session_id"])["host_token"][0]
		current_song = spotify_api.current_song_info(token)

		# current_song = {
		# 	"name": "New Light",
		# 	"artist": "John Mayer",
		# 	"img_url": "https://i.scdn.co/image/ab67616d0000b27321f02a52720857a42bba5417"
		# }
		queued_songs = [
			{"name": "WAP", "artist": "Cardi B"},
			{"name": "asdfasdf", "artist": "Ryan Mah"}
		]
		requested_songs = [
			{"name": "WAP", "artist": "Cardi B"}
		]

		return flask.render_template(
			"guest_dashboard.html",
			page_name = "Guest",
			session_id = flask.session["session_id"],
			current_song = current_song,
			# queued_songs = queued_songs,
			# requested_songs = requested_songs
		)

	else:
		return flask.abort(404)

@app_dashboard.route("/set-song-callback/<indx>")
def set_song_callback(indx):
	session_id = flask.session["session_id"]
	guest_user = spotify_api.get_username(flask.session["toke"])
	song_id = flask.session["songs_info"][int(indx)]["song_id"]
	curr_time = datetime.now()

	sql.add_queue(session_id, guest_user, song_id, curr_time)

	return flask.redirect(flask.url_for("app_dashboard.dashboard_guest"))


@app_dashboard.route("/search")
def search_song():
	songs = spotify_api.search(flask.session["toke"], flask.session["searched_song"])
	
	songs_info = []
	for i, song in enumerate(songs):
		temp = spotify_api.get_song_info_by_id(flask.session["toke"], song)
		temp["indx"] = i
		temp["song_id"] = song
		songs_info.append(temp)

	flask.session["songs_info"] = songs_info

	# return str(songs_info)
	return flask.render_template("search_results.html", session_id = flask.session["session_id"], songs = songs_info)
################################################################################################