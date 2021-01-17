function send_POST(obj) {
	var http = new XMLHttpRequest();
	url = window.location.href;

	// http.onreadystatechange = function() {
	// 	if (http.readyState == XMLHttpRequest.DONE) {
	// 		// console.log(http.responseText);
	// 		SERVER_RESPONSE = JSON.parse(http.responseText);
	// 	}
	// }
	http.open("POST", url, true);
	http.setRequestHeader("Content-type", "application/json");
	http.send(JSON.stringify(obj));
}

function remove_row(element) {
	if (document.getElementById("requested-table").rows.length - 1 == 0) { return; }
	var row = element.parentNode.parentNode.rowIndex;
	document.getElementById("requested-table").deleteRow(row);
}

function queue_song(element) {
	var table = document.getElementById("requested-table");
	var row = element.parentNode.parentNode.rowIndex;

	msg = {
		"command": "queue_song",
		"requested_by": table.rows[row].cells[0].innerHTML,
		"name": table.rows[row].cells[1].innerHTML,
		"artist": table.rows[row].cells[2].innerHTML
	};
	send_POST(msg);
	
	remove_row(element);
}

function remove_song(element) {
	var table = document.getElementById("requested-table");
	var row = element.parentNode.parentNode.rowIndex;

	msg = {
		"command": "remove_song",
		"requested_by": table.rows[row].cells[0].innerHTML,
		"name": table.rows[row].cells[1].innerHTML,
		"artist": table.rows[row].cells[2].innerHTML
	};
	send_POST(msg);

	remove_row(element);
}

function main() {
	// crude way of doing this, but ok for now
	setInterval(
		function() { window.location.reload(); },	// refresh every minute
		10*1000
		// 1000
	);
}
main();
