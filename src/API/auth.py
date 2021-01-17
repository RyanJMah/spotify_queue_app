import os
import sys
import requests

THIS_DIR = os.path.abspath(os.path.dirname(__file__))
PARENT_DIR = os.path.dirname(THIS_DIR)
sys.path.append(PARENT_DIR)

from credentials import *
#print(APP_SECRET_KEY)
API_BASE = "https://accounts.spotify.com"
REDIRECT_URI = "http://localhost/spotify_token_callback"
SCOPES = [
	"user-modify-playback-state",
	"user-follow-modify",
	"user-read-playback-state"
]

# def get_auth_url(redirect_uri, scopes, show_dialog = True):
# def get_auth_url(scopes, show_dialog = True):
def get_auth_url(show_dialog = True):
	auth_url = f'{API_BASE}/authorize'
	auth_url += f'?client_id={SPOTIFY_CLIENT_ID}'
	auth_url += f'&response_type=code'
	auth_url += f'&redirect_uri={REDIRECT_URI}'
	auth_url += f'&scope={",".join(SCOPES)}'
	if show_dialog:
		auth_url += f'&show_dialog={show_dialog}'

	return auth_url

# def get_auth_token(redirect_uri, code):
def get_auth_token(code):
	res = requests.post(
		f"{API_BASE}/api/token",
		data={
			"grant_type": "authorization_code",
			"code": code,
			"redirect_uri": REDIRECT_URI,
			# "redirect_uri": "http://localhost/spotify_token_callback",
			"client_id": SPOTIFY_CLIENT_ID,
			"client_secret": SPOTIFY_CLIENT_SECRET
		}
	)
	print(res.json())
	return res
