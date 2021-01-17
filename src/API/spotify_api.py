import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy.util as util
username = 'admin'
token = 'BQAklOXvdfJmo4l6Dtdyku87WQKB1hkHPO8WAoJkuvLANGz5-9-5dVX8cDHtwEE-sj8Mu7RloOZN4chnnY0yDmNOYDP8tZL5n_qxpbIrTv3sSJZUvk_8XgeUP57T_jfMhsvV3kOooH6Lv9xwJ8HZSLOPtqOWxwBhC2i9SlJ3i7OR'
sp = spotipy.Spotify(auth=token)
cid = "41e6ecfe5cd341e2b51fd54476a626e6"
secret = "1fca15b9415043db87a3571d1ecc90f9"
sp.add_to_queue('4l62h4tiuUwn7eD6hxMlVQ')
print(sp.current_user())
print(search('every day bro'))


def add_to_queue(uri, username, client_id, client_secret, redirect_uri):
    sp = spotipy.Spotify(auth=token)
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

    #make to add to not only actice device
    sp.add_to_queue(uri)

def user_info(username, client_id, client_secret, redirect_uri):
    if token:
        sp = spotipy.Spotify(auth=token)
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

        #make to add to not only actice device
        print(sp.current_user())

def search(q):
    results = sp.search(q, type='track', limit = 10, offset = 0, market = 'US')

    tracks = []
    for i in results['tracks']['items']:
        tracks.append(i['id'])

    return tracks




if __name__ == "__main__":

    #add_to_queue('0VjIjW4GlUZAMYd2vXMi3b', username, cid, secret, "http://localhost/")
    #user_info(username, cid, secret, "http://localhost/")
    #print(search('every day bro'))
    pass
#token = util.prompt_for_user_token(username, scope[1], client_id = cid, client_secret = secret, redirect_uri='http://localhost/')