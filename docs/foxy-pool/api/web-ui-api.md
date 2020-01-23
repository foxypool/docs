The Web-UI Socket.IO endpoint for every Foxy-Pool is reachable on

```
https://<hostname>.<tld>/web-ui
```

In the case of the main pools that would be `https://<coin>.foxypool.cf/web-ui`, where `<coin>`
needs to be substituted for the actual coin of the pool you want to connect to.

## API calls

### Retrieving all stats once

```javascript
const io = require('socket.io-client');

const client = io('https://bhd.foxypool.cf/web-ui');

client.emit('stats/init', ([poolConfig, poolStats, roundStats, liveStats]) => {
  // Do stuff here
});
```

### Subscribing to new stats

```javascript
...

client.on('stats/pool', (poolStats) => {
  // Do stuff here
});
client.on('stats/current-round', (roundStats) => {
  // Do stuff here
});
client.on('stats/live', (liveStats) => {
  // Do stuff here
});
```
