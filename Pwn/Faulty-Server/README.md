# Faulty server
> quasar-nova

## Description
I've somehow created a client-server application in C++, but can you check if it has any bug?
Use the client application to communicate with the server.

## Additional
+ This challenge has to be setup in a server
+ Locally, try to leak the flag without touching the binaries
+ Server usage:
	`./server <port> <workers>`
	Ports are bound to 0.0.0.0 (all interfaces)
+ Client usage:
	`./client <host> <port>`