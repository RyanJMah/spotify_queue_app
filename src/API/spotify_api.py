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

def add_to_queue(token, song_id, playlist_id, items):
    sp = spotipy.Spotify(auth=token)
    sp.add_to_queue(song_id)
    add_to_playlist(token, playlist_id, items)

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

def get_user_id(token):
    sp = spotipy.Spotify(auth=token)
    return sp.current_user()['id']

def create_playlist(token):
    sp = spotipy.Spotify(auth=token)
    playlist_id = sp.user_playlist_create(get_user_id(token), name = 'temp_Q', public = False)
    return playlist_id['id']

def add_to_playlist(token, playlist_id, items):
    sp = spotipy.Spotify(auth=token)
    sp.playlist_add_items(playlist_id, items)

def rem_from_playlist(token, playlist_id, items):
    sp = spotipy.Spotify(auth=token)
    sp.playlist_remove_all_occurrences_of_items(playlist_id, items)

if __name__ == "__main__":
    token = 'BQBoK34W-9CHbE24W7cppAWZyS0_4nl7XwQlr19PLWehWxdyAQkI5zh-Rert0tg2_UKbT2lYlUh-Ks2hE4OJtZFVdO3-xtpKcB8Kst4fhdM3_zk-ten61nhnSbPwelGbGVyZwzqjenpQahxNzexdkRX_dzIM3_pWz6gEMi4j2DEucg0MxOSL4OlpjB5K7Bq-lu9D_4Q1bw'
    id = create_playlist(token)
    add_to_playlist(token, id, ['5K9ka2I5o2T0tmFSpysNqW'])
    rem_from_playlist(token, id, ['4l62h4tiuUwn7eD6hxMlVQ'])
    #get_playlist_id(token)
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
