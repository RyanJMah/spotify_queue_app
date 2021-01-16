import requests

API_BASE = "https://accounts.spotify.com"

def auth():
	auth_url = f'{API_BASE}/authorize'
	auth_url += '?client_id={CLI_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}&show_dialog={SHOW_DIALOG}'