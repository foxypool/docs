## How to configure Foxy-Miner

Foxy-Miner looks for a file named `foxy-miner.yaml` in the current directory it is run from.
If no such file is found a first run wizard is shown which will create a basic `foxy-miner.yaml` based on your inputs.

## Configuration Options

The config file currently consists of these config options:

- `minerType`: Supported types are: `scavenger` or `conqueror` (**required**)
- `minerBinPath`: the binary path of scavenger / conqueror (**required**)
- `minerConfigPath`: the path to a custom miner config, will be passed with `-c /path/to/custom/config`
- `minerColor`: Set to a color to display for this miner in multi miner setups.
- `listenAddr`: a string representation of the address and port the miner should listen on and scavenger connect to (**required**)
- `noColors`: Disable colors.
- `humanizeDeadlines`: Set to true to show humanized deadlines instead of seconds.
- `logLevel`: Can be one of the following values: `error`, `info`, `debug`. Defaults to `info`.
- `useProfitability`: Set to true to use dynamic prios based on profitabilities of the coins.
- `maxNumberOfChains`: Set the max number of chains that should be scanning. Can be combined with `useProfitability` to only mine the `n` most profitable chains.
- `assumeScannedAfter`: Set to the number of seconds the miner should take at most, forces a chain switch when exceeded. Useful for miners where sometimes drives drop out and no `finished` line is printed.
- `accountColors`: Set your accountId to color associations here.
- `useEcoBlockRewards`: Set to true to enable eco block rewards for `useProfitability` option.
- `hideScanProgress`: Set to true to hide the miners scan progress. Useful for conqueror with pm2.
- `minerOutputToConsole`: Set to true to redirect all output of the miner directly to the console without processing/parsing it.
- `dashboardLogLines`: Defaults to 16, set the log lines used in the cli dashboard.
- `upstreams`: Array of upstream config objects, see below (**required**)
    - `name`: The name of the upstream, must be unique within the proxy (**required**)
    - `url`: The upstream url, should be omitted for foxy-pools
    - `updateMiningInfoInterval`: Change the default 1000 msec update interval, value is in ms. Only applies to HTTP polling based upstreams
    - `accountKey`: Add the supplied account key to miningInfo and nonceSubmission requests
    - `payoutAddress`: Your payout address, required for FoxyPool type upstreams.
    - `type`: Used to distinguish different upstream types. Valid values are `socketio` and `foxypool`. If the upstream is FoxyPool, set it to `foxypool`. If the upstream is a socket.io enabled Foxy-Proxy set it to `socketio`.
    - `minerName`: Set a custom miner name
    - `accountName`: Set a custom account name in FoxyPool
    - `sendTargetDL`: Set a custom targetDL to send to the miners
    - `weight`: defines which upstream should have the higher priority when two blocks appear within the same max scan time. Defaults to 10.
    - `minWeight`: If configured discard all new blocks with a weight below this value for this upstream
    - `color`: Use the defined hex string as color for this upstream's name. eg `'#e2ad58'`
    - `minerColor`: Send the defined hex string to this upstream as a per miner color.
    - `coin`: Required for `useProfitability`. Possible values are: `BHD`, `BURST`, `BOOM`, `DISC`, `LHD`.
    - `disabled`: Set to true to disable this upstream.
    - `submitProbability`: 95 for 95% submit probability per round (based on capacity and netDiff)
    - `doNotInterruptAbovePercent`: 80 for completing scans with this progress percentage even on higher prio chains.
    - `distributionRatio`: Your preferred distribution ratio (DR) on Foxy-Pools. Eg. `'50-50'` or `'100-0'`
    - `allowMiningToBeHalted`: Set to true to allow pools and foxy-miner to stop mining a coin should it not make sense to mine it currently (discarding block or btb oversize)
    - `walletUrl`: Can be configured with a BTB wallet to detect if we are oversize and should halt mining

- `miner`: An array of upstreams + miner configs, used only for multi miner setups
    - `upstreams`
    - `minerType`
    - `minerConfigPath`
    - `minerType`
    - `minerColor`

## Configuration Example

```yaml
minerBinPath: 'C:\\some\\path\\to\\scavenger.exe'
minerType: 'scavenger'
logLevel: 'info'
listenAddr: '127.0.0.1:5000'
humanizeDeadlines: true
upstreams:
  - name: 'FoxyPool BHD'
    type: 'foxypool'
    coin: 'BHD'
    payoutAddress: 'your BHD payout address'
    accountName: 'your desired name'
    weight: 12
    color: '#e25898'
    doNotInterruptAbovePercent: 95
  - name: 'FoxyPool BURST'
    type: 'foxypool'
    coin: 'BURST'
    payoutAddress: 'your BURST payout address'
    accountName: 'your desired name'
    weight: 8
    color: '#3c55d1'
    doNotInterruptAbovePercent: 95
```

[^1]: A wise man once said: "Knowledge is key"