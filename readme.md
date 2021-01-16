<h1>Design Document</h1>

<h2>Overview</h2>

The purpose of this application is to allow users to queue and vote for songs to be played. It's use cases include the following:

* Recreation centers
* Restaurants
* With friends

<h2>Requirements</h2>

<h3>User Roles</h3>

| User Role | Description                                           |
| --------- | ----------------------------------------------------- |
| Guest     | A device that queues and votes for songs for the host |
| Host      | The device that the music is actually playing on      |

<h3>Functional Requirements</h3>

| Requirement                                                  | Comments |
| ------------------------------------------------------------ | -------- |
| As a guest, you should be able to queue and vote for songs via the web client. | -        |
| As a host, you should have full control of the queue: deleting, moving, etc. | -        |
| As a guest, you should be able to connect to the web client via a QR code. | -        |
| As a host, you should be able to provide QR codes to guests. | -        |
| As a host, you should be able to set a preset playlist for when no songs are queued | -        |

<h3>Non-Functional Requirements</h3>

| Requirement                                      | Comments |
| ------------------------------------------------ | -------- |
| The UI should look good lol.                     | -        |
| Database should perform well, even under stress. | -        |

