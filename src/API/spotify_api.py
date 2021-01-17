import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy.util as util
import random
import string

username = 'admin'
token = 'BQD2R3QxQCSe7RMyFkvV0VGlVQ4eDdzBrwYVOKqEF8GInZp1kSkgLKQ9We5B1XG5lkGa5rv11Jsj5oMGsmhLPXfF4aeEhq-aLG_KGuoKP7Etv6E9iJatERHimMr-3aFxwBPlpstWt2vizkhR1knh06wP6kqlJRf643WHntRXM_sx9GmpuQ'
sp = spotipy.Spotify(auth=token)
cid = "41e6ecfe5cd341e2b51fd54476a626e6"
secret = "1fca15b9415043db87a3571d1ecc90f9"

def search(q):
    results = sp.search(q, type='track', limit = 5, offset = 0, market = 'US')

    tracks = []
    for i in results['tracks']['items']:
        tracks.append(i['id'])

    return tracks

def add_to_queue(song_id):
    sp.add_to_queue(song_id)
    
def skip_track():
    sp.next_track()

if __name__ == "__main__":
    pass
    #sp.add_to_queue('4l62h4tiuUwn7eD6hxMlVQ', device_id='780ae0669fd0cf51fe0cc44eb63c7b0694fc6340')
    #print(search('its every day bro'))
    #add_to_queue('4l62h4tiuUwn7eD6hxMlVQ')
    #print(sp.current_user())
