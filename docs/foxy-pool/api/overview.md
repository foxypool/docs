Foxy-Pools use [Socket.IO](https://socket.io) to communicate with miners and the Web-UI.

Socket.IO is a library that enables real-time, bidirectional and event-based communication between client and server.

This allows for low-overhead communication without the need for polling for new mining info or the latest pool stats.
Instead one can subscribe to topics one wants to be kept up-to-date with.
