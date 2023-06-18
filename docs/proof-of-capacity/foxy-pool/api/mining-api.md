## Socket.IO

The Mining Socket.IO endpoint of the Foxy-Pool Gateway is reachable on

```
http://miner.foxypool.io/mining
```

### Retrieving the current mining info for a given coin once

```javascript
const io = require('socket.io-client');

const client = io('http://miner.foxypool.io/mining');

const coin = 'SIGNA';
client.emit('getMiningInfo', coin, (miningInfo) => {
  // Do stuff here
});
```

### Subscribe to the coins you want to receive mining info for

```javascript
...

const coins = ['SIGNA'];
client.emit('subscribe', coins, () => {
  // Do stuff here
});
```

### Subscribing to new mining info

```javascript
...

client.on('miningInfo', (coin, miningInfo) => {
  // Do stuff here
});
```

### Submitting nonces

```javascript
...

// Regular submission format
const submission = {
  height: 12345,
  accountId: '12312134123123',
  nonce: '32462454345354',
  deadline: 1337,
};
// `options` encapsulates options otherwise sent via HTTP headers
const options = {
  minerName: 'Miner 1',
  accountName: 'My Name',
  payoutAddress: '33fKEwAHxVwnrhisREFdSNmZkguo76a2ML',
  userAgent: 'Foxy-Miner 1.13.0',
  capacity: 1337, // Capacity in GiB
  distributionRatio: '0-100',
};

const coin = 'SIGNA';
client.emit('submitNonce', coin, submission, options, (result) => {
  // Do stuff here
});
```

## Websockets

The Mining Websocket endpoint of the Foxy-Pool Gateway is reachable on

```
ws://miner.foxypool.io:8081
```

The Request format is JSON and has the following properties:

- **id**: the requests id is reused in the response for identification by the client, if it is supplied (optional)
- **coin**: the coin (eg. 'SIGNA') this request is referring to, **required** for 'getMiningInfo' and 'submitNonce' requests
- **topic**: 'getMiningInfo' or 'submitNonce' or 'subscribe'
- **payload**: the data to send with the request, **required** for 'submitNonce'

The Response format is JSON and has the following properties:

- **id**: the id from the request for identification by the client, if it was supplied
- **coin**: the coin (eg. 'SIGNA') this request is referring to
- **topic**: 'miningInfo' or 'submitNonce' or 'subscribe'
- **payload**: the result of the requests operation, only present when there was no error
- **error**: only present when an error happened, contains an error message



### Retrieving the current mining info for a given coin once

```javascript
const WebSocket = require('ws');

const client = new WebSocket('ws://miner.foxypool.io:8081');

// Wait for the connection to be open
await new Promise(resolve => client.onopen = resolve);
client.onopen = () => {};

// Helper function to send and receive messages which expect a response indicated by the same id
async function sendMessageAndAwaitResponse(messageToSend) {
  let handlerFunc = null;
  const result = await new Promise((resolve, reject) => {
    const expectResponse = ({ data: messageAsString }) => {
      const message = JSON.parse(messageAsString);
      if (message.id !== messageToSend.id) {
        return;
      }
      if (message.error) {
        return reject(message.error);
      }
      resolve(message.payload);
    };
    handlerFunc = expectResponse;
    client.addEventListener('message', expectResponse);

    client.send(JSON.stringify(messageToSend));
  });
  client.removeEventListener('message', handlerFunc);
  handlerFunc = null;

  return result;
}

const coin = 'SIGNA';
const miningInfo = await sendMessageAndAwaitResponse({
  id: 123,
  coin,
  topic: 'getMiningInfo',
});
// Do stuff here
```

### Subscribe to the coins you want to receive mining info for

```javascript
...

const coins = ['SIGNA'];
await sendMessageAndAwaitResponse({
  id: 123,
  topic: 'subscribe',
  payload: coins,
});
```

### Subscribing to new mining info

```javascript
...

client.on('message', (messageAsString) => {
  const message = JSON.parse(messageAsString);
  if (message.topic !== 'miningInfo') {
    return;
  }
  const coin = message.coin;
  const miningInfo = message.payload;
  // Do stuff here
});
```

### Submitting nonces

```javascript
...

// Regular submission format
const submission = {
  height: 12345,
  accountId: '12312134123123',
  nonce: '32462454345354',
  deadline: 1337,
};
// `options` encapsulates options otherwise sent via HTTP headers
const options = {
  minerName: 'Miner 1',
  accountName: 'My Name',
  payoutAddress: '33fKEwAHxVwnrhisREFdSNmZkguo76a2ML',
  userAgent: 'Foxy-Miner 1.13.0',
  capacity: 1337, // Capacity in GiB
  distributionRatio: '0-100',
};

const coin = 'SIGNA';
const result = await sendMessageAndAwaitResponse({
  id: 123,
  coin,
  topic: 'submitNonce',
  payload: {
    submission,
    options,
  },
});
// Do stuff here
```
