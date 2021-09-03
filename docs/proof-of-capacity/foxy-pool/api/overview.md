Foxy-Pools support several connection methods to use by miners and use HTTP and Socket.IO for the stats API.

- [Socket.IO](https://socket.io), a library that enables real-time, bidirectional and event-based communication between client and server.
- plain Websockets
- HTTP polling

Socket.IO and plain Websockets allow for low-overhead communication without the need for polling for new mining info or the latest pool stats.
Instead one can subscribe to topics one wants to be kept up-to-date with.
