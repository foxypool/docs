## How to configure Foxy-Proxy

Foxy-Proxy looks for a file named `config.yaml` in the current directory it is run from.
If no such file is found it will look for it in `<HOMEDIR>/.config/foxy-proxy/config.yaml`.

If no config file can be found, an example config file is created for you in `<HOMEDIR>/.config/foxy-proxy/config.yaml`.

To store statistics Foxy-Proxy uses a SQLite database located in `<HOMEDIR>/.config/foxy-proxy/db.sqlite` by default.

## Autostart Foxy-Proxy on boot

### Windows

!!! info
    The following steps for Windows will start the proxy on login, not boot

1. Create a `.bat` file which contains the following lines:
```
cls
:start
call foxy-proxy
goto start
```

2. Create a shortcut to that bat file and move it into `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

### Linux

1. Install pm2:
```
npm i -g pm2
```

2. Start the proxy through pm2:
```
pm2 start foxy-proxy
```

3. Save the current running configuration and create a startup cmd:
```
pm2 save
pm2 startup
```

4. Depending on if you are `root` the `pm2 startup` command either runs directly or outputs a sudo command you will need to execute.


## Configuration Options

The config file currently consists of these config options:

- `proxies`: Array of proxy config objects, see below (**required**)
    - `name`: The name of the proxy, must be unique (**required**)
    - `maxScanTime`: The maximum amount of seconds each round takes to scan completely. Defaults to 30 seconds.
    - `ignoreMinerIP`: Only use the miners name for identification, useful for Heroku deployments.
    - `color`: Use the defined hex string as color for this proxy's name. eg `'#e2ad58'`
    - `minerColor`: Use the defined hex string as color for this proxies's miner names in logs. eg `'#e2ad58'`
    - `minerOfflineMinutes`: Report miners offline after at least this amount of minutes. Defaults to 5.
    - `minerOfflineBlocks`: Report miners offline after at least this amount of blocks. Defaults to 2.
    - `hideUpstreamName`: Set to true to hide the upstreams name in logs. Useful for single upstream proxies.
    - `humanizeDeadlines`: Set to true to display deadlines in the cli in a human readable format (2d 02:46:13).
    - `dynamicDeadlineColor`: Set to true to use dynamic colors from red to green for deadlines.
    - `dynamicDeadlineColorLimit`: Set the deadline limit from where on deadlines are considered "bad" and colored red. Defaults to 2678400 (31 days).
    - `disabled`: Set to true to disable the proxy.
    - `useProfitability`: Set to true to use dynamic prios based on profitabilities of the coins.
    - `useEcoBlockRewards`: Set to true to enable eco block rewards for useProfitability option.
    - `maxNumberOfChains`: Set the max number of chains that should be scanning. Can be combined with `useProfitability` to only mine the `n` most profitable chains.
    - `upstreams`: Array of upstream config objects, see below (**required**)
        - `name`: The name of the upstream, must be unique within the proxy (**required**)
        - `url`: The upstream url, should be omitted for foxy-pools
        - `mode`: `'solo'` or `'pool'` depending on if the upstream is a pool or a solo wallet (**required**)
        - `isBHD`: Set to `true` if the upstream is a bhd solo wallet or bhd pool (**required** for bhd based upstreams)
        - `walletUrl`: Optional url of a wallet to retrieve block winner information
        - `customEndpoint`: Set a custom endpoint for burst like coins. Defaults to `burst`. Set to `boom` for the boomcoin wallet.
        - `passphrases`: accountId -> passphrase mapping for solo mining (**required** for solo)
        - `passphrase`: Use a singular passphrase for all accountIds (pool emulation)
        - `targetDL`: Deadlines below this value will not be sent to the upstream (**required**)
        - `updateMiningInfoInterval`: Change the default 1000 msec update interval, value is in ms
        - `accountKey`: Add the supplied account key to miningInfo and nonceSubmission requests (**required** for bhd pools)
        - `payoutAddress`: Your payout address, required for FoxyPool type upstreams.
        - `type`: Used to distinguish different upstream types. Valid values are `foxypool` and `socketio`. Omit to use the generic upstream.
        - `accountIdToUrl`: accountId -> upstream url (object), override the default upstream url based on the accountId
        - `historicalRoundsToKeep`: By default keep 720 rounds of historical stats, overwrite here
        - `minerName`: Set a custom miner name
        - `accountName`: Set a custom account name in FoxyPool
        - `sendTargetDL`: Set a custom targetDL to send to the miners
        - `submitProbability`: Set to the desired percentage you want to submit with, eg 0.95 for 95% submits.
        - `weight`: defines which upstream should have the higher priority when two blocks appear within the same max scan time. Defaults to 10.
        - `sendMiningSoftwareName`: When set to true send the mining software name as well on submit nonce requests.
        - `accountIdToTargetDL`: accountId -> targetDL (object), override the upstream-wide configured targetDL for specific account ids.
        - `showAllDeadlines`: set to true to show all DLs received by the proxy.
        - `color`: Use the defined hex string as color for this upstream's name. eg `'#e2ad58'`
        - `newBlockLineColor`: Use the defined hex string as color for this upstream's new block lines. eg `'#e2ad58'`
        - `newBlockColor`: Use the defined hex string as color for this upstream's new block height. eg `'#e2ad58'`
        - `newBlockBaseTargetColor`: Use the defined hex string as color for this upstream's new block baseTarget. eg `'#e2ad58'`
        - `newBlockNetDiffColor`: Use the defined hex string as color for this upstream's new block netDiff. eg `'#e2ad58'`
        - `newBlockTargetDeadlineColor`: Use the defined hex string as color for this upstream's new block targetDeadline. eg `'#e2ad58'`
        - `minerColor`: Use the defined hex string as color for this upstream's miner names in logs. eg `'#e2ad58'`
        - `accountColor`: Use the defined hex string as color for this upstream's accountIds in logs. eg `'#e2ad58'`
        - `accountColors`: Use the defined hex string as color per accountId for this upstream in logs. eg `'1234': '#e2ad58'`
        - `deadlineColor`: Use the defined hex string as color for this upstream's deadlines in logs. eg `'#e2ad58'`
        - `estimatedCapacityRounds`: Use a custom amount of rounds for estimated capacity calculations.
        - `disabled`: Set to true to disable the upstream.
        - `coin`: Required for `useProfitability` and correct block explorer links. Possible values are: `BHD`, `BURST`, `DISC`, `LHD`, `XHD`, `HDD`.
        - `excludedAccountIds`: An array of accountIds to exclude when submitting to the upstream.
        - `distributionRatio`: Your preferred distribution ratio (DR) on Foxy-Pools. Eg. `'50-50'` or `'100-0'`
        - `minerPassthrough`: Set to true to pass the miners minerName and capacity through to the upstream.
- `listenAddr`: a string representation of the address and port the proxy should listen on (**required**)
- `useMultiplePorts`: set this to `true` when using blago as blago doesn't support regular urls but only an address and a port
- `webAuth`: Remove this config option to allow any user without authenticating to access the stats
    - `username`: The username to use for logging in
    - `password`: The password to use for logging in, will be removed by the proxy and replaced with a `passHash` value to never store your password in plain text.
- `logLevel`: Can be one of the following values: `error`, `info`, `debug`. Defaults to `info`.
- `logToFile`: Boolean, if set to `true` logs to `proxy.log` in the default log location (`<HOMEDIR>/.config/foxy-proxy/logs`). Files are rotated once they reach 10MB and each day.
- `logDir`: Override the default log directory with a custom one
- `logMaxFiles`: Set the number of log files to keep, eg. 5 to keep only the last 5 log files
- `mail`: Contains config keys required for sending miner offline/recovered mails.
    - `host`: The hostname of the smtp mail server, eg. `smtp.googlemail.com`
    - `port`: The port to use when sending mails, eg `465`
    - `secure`: Boolean value whether to use TLS/SSL or not
    - `user`: The username/mail address to authenticate with
    - `pass`: The password to authenticate with
    - `mailTo`: The recipient mail address
    - `mailFrom`: Optional config key to override the user as sender
- `disableAnonymousStatistics`: Set to true to disable anonymous usage statistics.
- `automaticUpdates`: Set to true to enable automatic updates once a new version is detected. Works for npm and git installs.
- `isInstalledGlobally`: Set to true if you installed the proxy globally via npm.
- `transports`: An array of transports to use. Available options are: `http` and `socket.io`.

## Configuration Example

```yaml
listenAddr: '127.0.0.1:12345'
useMultiplePorts: false
proxies:
  - name: 'Multi-Foxy'
    maxScanTime: 30
    upstreams:
      - name: 'FoxyPool BHD'
        type: 'foxypool'
        coin: 'BHD'
        payoutAddress: 'your BHD payout address'
        accountName: 'your desired name'
        weight: 12
      - name: 'FoxyPool BURST'
        type: 'foxypool'
        coin: 'BURST'
        payoutAddress: 'your BURST payout address'
        accountName: 'your desired name'
        weight: 8
```
