The Mining Socket.IO endpoint for every Foxy-Pool is reachable on

```
https://<hostname>.<tld>/mining
```

In the case of the main pools that would be `https://<coin>.foxypool.cf/mining`, where `<coin>`
needs to be substituted for the actual coin of the pool you want to connect to.

## API calls

### Retrieving the current mining info once

```javascript
const io = require('socket.io-client');

const client = io('https://bhd.foxypool.cf/mining');

client.emit('getMiningInfo', (miningInfo) => {
  // Do stuff here
});
```

### Subscribing to new mining info

```javascript
...

client.on('miningInfo', (miningInfo) => {
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

client.emit('submitNonce', submission, options, (result) => {
  // Do stuff here
});
```

### Retrieving the block winner account id for a given height

```javascript
...

client.emit('getBlockWinnerAccountId', height, (accountId) => {
  // Do stuff here
});
```
