The Web-UI Socket.IO endpoint of the Foxy-Pool Gateway is reachable on

```
https://api.foxypool.cf/web-ui
```

## Retrieving all stats once for a given pool by hostname

```javascript
const io = require('socket.io-client');

const client = io('https://api.foxypool.cf/web-ui');

const hostname = 'bhd.foxypool.cf';
client.emit('stats/init', hostname, ([poolConfig, poolStats, roundStats, liveStats]) => {
  // Do stuff here
});
```

## Subscribe to new pool stats for a given list of pools by hostname

```javascript
...

const hostnames = ['bhd.foxypool.cf', 'burst.foxypool.cf'];
client.emit('subscribe', hostnames, () => {
  // Do stuff here
});
```

## Subscribing to new stats

```javascript
...

client.on('stats/pool', (hostname, poolStats) => {
  // Do stuff here
});
client.on('stats/round', (hostname, roundStats) => {
  // Do stuff here
});
client.on('stats/live', (hostname, liveStats) => {
  // Do stuff here
});
```
