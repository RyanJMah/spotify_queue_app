import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
import spotipy.util as util

def add_to_queue(uri, username, client_id, client_secret, redirect_uri):
    scope = 'user-modify-playback-state'
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

        #make to add to not only actice device
        sp.add_to_queue(uri)
    else:
        print("Can't get token for", username)

def user_info(username, client_id, client_secret, redirect_uri):
    scope = 'user-follow-modify'
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        sp = spotipy.Spotify(auth=token)
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)

        #make to add to not only actice device
        print(sp.current_user())
    else:
        print("Can't get token for", username)

def search(q):
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=cid, client_secret=secret))
    results = sp.search(q='The weekend', type='track', limit = 10, offset = 0, market = 'US')

    tracks = []
    for i in results['tracks']['items']:
        tracks.append(i['id'])

    return tracks


cid = 'e928528d94e84800aa53f32758c82ccc'
secret = 'f5ee15641c8c41e6a4bb2541cde6765c'

#Ryan
#cid = '41e6ecfe5cd341e2b51fd54476a626e6'
#secret = '1fca15b9415043db87a3571d1ecc90f9'

if __name__ == "__main__":
    '''
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()
    '''
    playlist_id = None
    username = input('username: ')
    if playlist_id != None:
        sp.playlist_add_items(playlist_id, items, position=None)
    else:
        user_playlist_create(username, 'Suggested Songs', public = False, collaborative = False, description ='Songs yet to be approved')
        print(user_playlists()) #use this to get the playlist id
    #add_to_queue('0VjIjW4GlUZAMYd2vXMi3b', username, cid, secret, "http://localhost/")
    #user_info(username, cid, secret, "http://localhost/")
    #print(search('despacito'))


#token = util.prompt_for_user_token(username, scope[1], client_id = cid, client_secret = secret, redirect_uri='http://localhost/')
