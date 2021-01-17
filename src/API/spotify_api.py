import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import random
import string

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)

from credentials import *

#cid = "41e6ecfe5cd341e2b51fd54476a626e6"
#secret = "1fca15b9415043db87a3571d1ecc90f9"

def search(token, q):
	sp = spotipy.Spotify(auth=token)

	results = sp.search(q, type='track', limit = 5, offset = 0, market = 'US')
	tracks = []
	for i in results['tracks']['items']:
		tracks.append(i['id'])

	return tracks

def add_to_queue(token, song_id):
	sp = spotipy.Spotify(auth=token)
	sp.add_to_queue(song_id)

def skip_track(token):
	sp = spotipy.Spotify(auth=token)
	sp.next_track()

def current_song_info(token):
	sp = spotipy.Spotify(auth=token)
	info = sp.current_playback()
	# print(info)
	if info is None:
		return None

	artists = ''
	for artist in info['item']['artists']:
		if artists == '':
			artists = artist['name']
		else:
			artists = artists + ', ' + artist['name']

	# print(artists)
	return {'name':info['item']['name'], 'artist':artists, 'img_url':info['item']['album']['images'][0]['url'], "song_id": info["item"]["id"]}
	# return {'name':info['item']['name'], 'artist':artists, 'img_url':info['item']['album']['images'][0]['url'], "song_id": info["item"]["id"]}

def get_song_info_by_id(token, song_id):
	sp = spotipy.Spotify(auth=token)
	info = sp.track(song_id)
	# print(info)
	ret = {
		"artist": ", ".join( [i["name"] for i in info["album"]["artists"]] ),
		"name": info["name"],
		"img_url": info["album"]["images"][0]["url"]
	}
	return ret

def search_song_info(token, song_id):
	sp = spotipy.Spotify(auth=token)
	info = sp.track(song_id)
	print(info)

	artists = ''
	for artist in info['item']['artists']:
		if artists == '':
			artists = artist['name']
		else:
			artists = artists + ', ' + artist['name']

	return {'name':info['item']['name'], 'artist':artists, 'img_url':info['item']['album']['images'][0]['url']}

def get_username(token):
	sp = spotipy.Spotify(auth = token)
	return sp.current_user()["display_name"]


def get_user_id(token):
	sp = spotipy.Spotify(auth = token)
	return sp.current_user()['id']

def create_playlist(token):
	sp = spotipy.Spotify(auth = token)
	playlist_id = sp.user_playlist_create(get_user_id(token), name = 'temporary_groupify_playlist', public = False)
	return playlist_id['id']

def del_playlist(token, playlist_id):
	sp = spotipy.Spotify(auth = token)
	sp.current_user_unfollow_playlist(playlist_id)

def add_to_playlist(token, playlist_id, items):
	sp = spotipy.Spotify(auth = token)
	sp.playlist_add_items(playlist_id, items, position = len(sp.playlist(playlist_id)['tracks']['items']))

def rem_from_playlist(token, playlist_id, items):
	sp = spotipy.Spotify(auth = token)
	sp.playlist_remove_all_occurrences_of_items(playlist_id, items)

# def get_playlist_queue(token, playlist_id):
# 	sp = spotipy.Spotify(auth = token)

# 	playlist_length = len(sp.playlist(playlist_id)['tracks']['items'])
# 	#Hardcoded for now
# 	song_position = 0
# 	temp = sp.playlist(id)['tracks']['items']
# 	ret = []
# 	if(playlist_length - song_position < 5):
# 		for i in range(song_position,playlist_length-1,1):
# 			ret.append(get_song_info_by_id(token, temp[i]['track']['id']))
# 	else:
# 		for i in range(song_position,5+song_position,1):
# 			ret.append(get_song_info_by_id(token, temp[i]['track']['id']))
# 	#print(ret)
# 	return ret

def get_pos_by_id(token, song_id):
	sp = spotipy.Spotify(auth=token)
	pos = 0
	for i in sp.playlist(id)['tracks']['items']:
		if (i['track']['id'] == song_id):
			return pos
		pos += 1
	return None

# def get_playlist_queue(token, playlist_id, song_id):
# 	sp = spotipy.Spotify(auth=token)

# 	playlist_length = len(sp.playlist(playlist_id)['tracks']['items'])
# 	#Hardcoded for now
# 	song_position = get_pos_by_id(token, song_id)
# 	temp = sp.playlist(id)['tracks']['items']
# 	ret = []
# 	if(playlist_length - song_position < 5):
# 		for i in range(song_position,playlist_length-1,1):
# 			ret.append(get_song_info_by_id(token, temp[i]['track']['id']))
# 	else:
# 		for i in range(song_position,5+song_position,1):
# 			ret.append(get_song_info_by_id(token, temp[i]['track']['id']))
# 	#print(ret)
# 	return ret
def playlist_song_titles(token, playlist_id):
    sp = spotipy.Spotify(auth=token)
    info = sp.playlist_items(playlist_id)

    song_names = []
    for song in info['items']:
        song_names.append(song['track']['name'])
    return song_names

def get_playlist_queue(token, playlist_id):
    sp = spotipy.Spotify(auth=token)

    song_position = 0
    song = current_song_info(token)
    current_song = song['name']
    #search within list of playlist to find current_song position
    songlist = playlist_song_titles(token, playlist_id)  
    for position in range(len(songlist)):
        if current_song == songlist[position]:
            song_position = position + 1
            break
    
    tracklist = sp.playlist_tracks(playlist_id, fields = None, limit = 5, offset = song_position, market = None)

    queue = []
    if (tracklist["total"] - song_position) < 5:
        for i in range(tracklist["total"] - song_position):
            song_id = tracklist['items'][i]['track']['id']
            info = get_song_info_by_id(token, song_id)
            queue.append(info)
    else:
        for i in range(5):
            song_id = tracklist['items'][i]['track']['id']
            # Dic['item']['track']['id']
            info = get_song_info_by_id(token, song_id)
            queue.append(info)

    return queue


if __name__ == "__main__":
	# token = 'BQBnwEVux0M9ywTT279zRsH3qBH6K6sqqqN2xis9YEA1n6VBlpgsr1_k-KeVGP4wyunVYGAi06VtWXKCgUV3GikMc5PrxQ_zOyMOSHJsHxuZHkK5Dn8-3AMWqtGY1Fe_gG1iiIMFq0p7IJ1YqrdtGQ7RIckvuV8Lck_9_t1ixmdvow'
	token = "BQDLveaLWlHV0e_HE8ybASguItETsBPfLyPP1txUNO5Q7z789oRwDOcG5AjT7dNU54QIePB5xWTt4VSCSiIM986YwIl9LNj5pSVgX7jqfbWMvxAzekC-glv2SEEQuDEOPNfr0XbSSOyJiHwTpdLTf2SnIVx-LTFc0xxuPb6Nucj9OTbRvYN8Xpb3vuz_wOHr6qPMrtlmTxjj13wu80D59J7JbBj0lF4"
	#print(search(token, "john mayer"))
	#sp.add_to_queue('4l62h4tiuUwn7eD6hxMlVQ', device_id='780ae0669fd0cf51fe0cc44eb63c7b0694fc6340')
	#print(search('its every day bro'))
	#add_to_queue('4l62h4tiuUwn7eD6hxMlVQ')
	#print(sp.current_user())
	#print(sp.current_user())
	#print(sp.current_user())
	# print(current_song_info(token))
	# print(get_user_info(token))
	# playlist_id = create_playlist(token)
	# print(get_playlist_queue())
	#search_song_info(token, '4l62h4tiuUwn7eD6hxMlVQ')
	pass