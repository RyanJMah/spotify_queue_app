// URL = "http://localhost/login"

function authenticate() {
	var http = new XMLHttpRequest();
	url = window.location.href;
	console.log(url)

	http.onreadystatechange = function() {
		if (http.readyState == XMLHttpRequest.DONE) {
			// console.log(http.responseText);
			window.location.href = http.responseText;
		}
	}
	http.open("POST", url, true);
	http.setRequestHeader("Content-type", "application/json");
	http.send(JSON.stringify({"attempting_login": true}));
}