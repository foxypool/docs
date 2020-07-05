## How to configure Pledge-Agent

Pledge-Agent looks for a file named `pledge-agent.yaml` in the current directory it is run from.
If no config file can be found, an example config file is created for you.

## Configuration Options

The config file currently consists of these config options:

- `<coin>`: The coin name in caps, valid coins are listed [here](supported-coins.md)
    - `sendTo`: The address to send coins to, can be omitted if no sending is desired. Can be an array where the first entry is the address and the second entry is the percentage to use
    - `pledgeTo`: The address to pledge coins to, can be omitted if no pledging is desired. Can be an array where the first entry is the address and the second entry is the percentage to use
    - `sendThreshold`: The minimum amount to send
    - `pledgeThreshold`: The minimum amount to pledge
    - `walletUrl`: The wallet url to use (only BURST)
    - `accountIdToPassPhrase`: The numeric accountId to passphrase mapping (only BURST) to use for sending / pledging
    - `walletUrls`: The wallet urls (array) to use (only BHD, DISC, HDD, LHD, XHD). Entries can be strings (a wallet url) or an object with the following properties:
        - `url`: The wallet url to use
        - `walletPassphrase`: The passphrase for the wallet
    - `sendMessage`: The message to add when sending coins (only BURST)
    - `moveOtherPledges`: If set to true will cancel pledges pointing at addresses different form the currently configured `pledgeTo` address
    - `maxPledge`: Make sure to pledge at most this many coins to the configured `pledgeTo` address in total
    - `lockingPeriod`: Set the amount to lock the pledges for (only XHD). Use a string with an english time duration like `'9 months'` or set the amount of blocks to lock for as integer.
    - `coinsToKeepInWallet`: The amount of coins to keep in the wallet and not send / pledge
    - `multiplesOf`: Only send/pledge amounts that are multiples of this number.

## Configuration Example

```yaml
BHD:
  pledgeTo: '382huZpCbisipKsLWTyQoPeWcpeeBRVdFF'
  walletUrls:
  - url: 'http://someuser:somepass@127.0.0.1:8732'
    walletPassphrase: 'for encrypted wallets'
  pledgeThreshold: 1
  moveOtherPledges: false
BURST:
  sendTo: 'BURST-BVUD-7VWE-HD7F-6RX4P'
  accountIdToPassPhrase:
    '1234567890': 'my secret passphrase here'
  walletUrl: 'http://127.0.0.1:8125'
  sendThreshold: 0
DISC:
  pledgeTo: ['1LLB4uVBUEgr9ERGoHV2tLaYFnQjfak7K3', 70]
  sendTo: ['1F9nVpiA7iKcrpyHCGw6AeqMdU9EebZmrw', 30]
  walletUrls:
  - 'http://someuser:somepass@127.0.0.1:63336'
  pledgeThreshold: 5
  sendThreshold: 5
  moveOtherPledges: true
LHD:
  pledgeTo: '31j58GwZ7QujCrwvsrhppvc8MFvRtQ8g7r'
  walletUrls:
  - 'http://someuser:somepass@127.0.0.1:9832'
  pledgeThreshold: 1
  moveOtherPledges: true
HDD:
  pledgeTo: '3PFZGaoP2eZHjcE6bivCodZTwVChbo1Woz'
  walletUrls:
  - 'http://hddcash:aWJGS22RctmT9Wh8uptX@127.0.0.1:6332'
  pledgeThreshold: 1
  moveOtherPledges: true
XHD:
  pledgeTo: '3BavJsWWGmDd1ZBzNGQV8ejkqXLXntdMsy'
  walletUrls:
  - 'http://someuser:somepass@127.0.0.1:8032'
  pledgeThreshold: 1
  moveOtherPledges: true
  lockingPeriod: '9 months'
```

## Configuring the wallets

Some wallets require you to configure them to allow API access through pledge-agent:

### BHD

You'll need to create/edit the file `btchd.conf` (located in `C:\Users\<user>\AppData\Roaming\btchd` on Windows) with the following content:
```
rpcuser=someuser
rpcpassword=somepass
server=1
rpcallowua=1
```

### LHD

You'll need to create/edit the file `ltchd.conf` (located in `C:\Users\<user>\AppData\Roaming\ltchd` on Windows) with the following content:
```
rpcuser=someuser
rpcpassword=somepass
server=1
```

### XHD

You'll need to create/edit the file `xrphd.conf` (located in `C:\Users\<user>\AppData\Roaming\xrphd` on Windows) with the following content:
```
rpcuser=someuser
rpcpassword=somepass
server=1
```

### HDD

You'll need to create/edit the file `hddcash.conf` (located in `C:\Users\<user>\AppData\Roaming\hddcash` on Windows) with the following content:
```
rpcuser=hddcash
rpcpassword=aWJGS22RctmT9Wh8uptX
server=1
```

### DISC

You'll need to create/edit the file `diskcoin.conf` (located in `C:\Users\<user>\AppData\Roaming\diskcoin` on Windows) with the following content:
```
rpcuser=someuser
rpcpassword=somepass
server=1
```
