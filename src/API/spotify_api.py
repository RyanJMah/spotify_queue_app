import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy.util as util
import random
import string
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

if __name__ == "__main__":
    token = 'BQC-pBzh26INfN3SbPrf0u1YSZf7ZmTcYFDd2r3PqTft3cXPGBmKp9lV-o7xa01NAf6oVU5teqJJGBc5Jl3j6Erasc9FicpXuhaVjiy1S8rGG2sv7pAuTPWjT2PsdYOP7nMI5Wzo47XejAshWae1z1zhsl10'
    search(token, "john mayer")
    #sp.add_to_queue('4l62h4tiuUwn7eD6hxMlVQ', device_id='780ae0669fd0cf51fe0cc44eb63c7b0694fc6340')
    #print(search('its every day bro'))
    #add_to_queue('4l62h4tiuUwn7eD6hxMlVQ')
    #print(sp.current_user())
