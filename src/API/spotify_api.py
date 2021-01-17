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

def current_song_info(token):
    sp = spotipy.Spotify(auth=token)
    info = sp.current_playback()

    artists = ''
    for artist in info['item']['artists']:
        if artists == '':
            artists = artist['name']
        else:
            artists = artists + ', ' + artist['name']

    print(artists)

    return {'name':info['item']['name'], 'artist':artists, 'img_url':info['item']['album']['images'][0]['url']}

def search_song_info(token, song_id):
    sp = spotipy.Spotify(auth=token)
    info = sp.track(song_id)

    artists = ''
    for artist in info['item']['artists']:
        if artists == '':
            artists = artist['name']
        else:
            artists = artists + ', ' + artist['name']

    return {'name':info['item']['name'], 'artist':artists, 'img_url':info['item']['album']['images'][0]['url']}


if __name__ == "__main__":
    token = 'BQBnwEVux0M9ywTT279zRsH3qBH6K6sqqqN2xis9YEA1n6VBlpgsr1_k-KeVGP4wyunVYGAi06VtWXKCgUV3GikMc5PrxQ_zOyMOSHJsHxuZHkK5Dn8-3AMWqtGY1Fe_gG1iiIMFq0p7IJ1YqrdtGQ7RIckvuV8Lck_9_t1ixmdvow'
    #print(search(token, "john mayer"))
    #sp.add_to_queue('4l62h4tiuUwn7eD6hxMlVQ', device_id='780ae0669fd0cf51fe0cc44eb63c7b0694fc6340')
    #print(search('its every day bro'))
    #add_to_queue('4l62h4tiuUwn7eD6hxMlVQ')
    #print(sp.current_user())
    #print(sp.current_user())
    #print(sp.current_user())
    #current_song_info(token)
    #search_song_info(token, '4l62h4tiuUwn7eD6hxMlVQ')
    pass
