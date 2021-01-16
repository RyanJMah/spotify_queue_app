function authenticate() {
	redirect_uri = "http://localhost"
	url = 'https://accounts.spotify.com/authorize' +
	      '?response_type=code' +
          '&client_id=' + my_client_id +
          (scopes ? '&scope=' + encodeURIComponent(scopes) : '') +
          '&redirect_uri=' + encodeURIComponent(redirect_uri);

	http = new XMLHttpRequest();
	url = window.location.href;
	
	http.open("POST", url, true);
	http.setRequestHeader("Content-type", "application/json");
	http.send(JSON.stringify({"attempting_login": true}));
}