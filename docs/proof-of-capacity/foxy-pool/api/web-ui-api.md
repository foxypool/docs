## HTTP API

Check out the API docs here: [api-docs.foxypool.io](https://api-docs.foxypool.io/?urls.primaryName=Proof-of-Capacity%20(PoC)){target=_blank}

## Socket.IO API

The Web-UI Socket.IO endpoint of the Foxy-Pool Gateway is reachable on

```
https://api.foxypool.io/web-ui
```

To interact with a specific pool you will need the pools poolIdentifier. The poolIdentifier is generally the subdomain part of the hostname. For example the BHD pools poolIdentifier is `bhd`.

## Subscribe to new pool stats for a given list of pools by pool identifier

```javascript
const io = require('socket.io-client');

const client = io('https://api.foxypool.io/web-ui');

const poolIdentifier = ['bhd', 'signa'];
client.emit('subscribe', poolIdentifier, () => {
  // Do stuff here
});
```

## Subscribing to new stats

```javascript
...

client.on('stats/round', (poolIdentifier, roundStats) => {
  // Do stuff here
});
client.on('stats/live', (poolIdentifier, liveStats) => {
  // Do stuff here
});
```
