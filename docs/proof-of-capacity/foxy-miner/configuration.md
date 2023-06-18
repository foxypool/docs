## Configuration Location

The Foxy-Miner config (`foxy-miner.yaml`) is located in your home directory in the `.config/foxy-miner` subdirectory. For example on Windows:

    C:\Users\<User>\.config\foxy-miner\foxy-miner.yaml

## Configuration Loading

Foxy-Miner first checks if a config is available in the users home directory (see above), then in the current directory it is run from and finally if no configs can be found a first run wizard is shown which will guide the user through the setup process.

## Configuration Example

```yaml
logLevel: info
logToFile: true
humanizeDeadlines: true
isCpuOnly: false
upstreams:
  - name: 'FoxyPool SIGNA'
    type: 'foxypool'
    coin: 'SIGNA'
    payoutAddress: 'your SIGNA payout address'
    accountName: 'your desired name'
    weight: 8
    color: '#3c55d1'
    doNotInterruptAbovePercent: 95
minerConfig:
  useHddDirectIo: true
  cpuWorkers: 0
  useCpuThreadPinning: false
  gpuPlatform: 0
  gpuDevice: 0
  gpuThreads: 1
  gpuWorkers: 12
  gpuNoncesPerCache: 262144
  useGpuMemMapping: false
  useGpuAsyncCompute: true
  plotDirs:
    - D:\
    - E:\
    - F:\
listenAddr: 127.0.0.1:5000
isManaged: true
minerType: scavenger
```

## Configuration Options

The config file currently consists of these config options:

### `logLevel`
: Possible values: `error`, `info`, `debug` or `trace`. Defaults to `info`.

### `logToFile`
: Possible values: `true`, `false`. When set to `true` logs to `<HOMEDIR>/.config/foxy-miner/logs/foxy-miner.log`. Files are rotated once they reach 10MB and each day.

### `humanizeDeadlines`
: Possible values: `true`, `false`. When set to `true` Foxy-Miner will show deadlines in `d hh:mm:ss` instead of seconds.

### `isCpuOnly`
: Possible values: `true`, `false`. Determines whether to use a miner compiled with OpenCL support or without. Some systems do not have a GPU or OpenCL support and need to use this option.

### `upstreams`
: A list of upstreams. Upstreams are generally pools.
    #### `name`
    : Possible values: Any string. The name of the upstream.
    #### `type`
    : Possible values: `socketio`, `foxypool`. Used to distinguish different upstream types. When omitted legacy http polling is used.
    #### `coin`
    : Possible values: `SIGNA`. Required for Foxy-Pools and the `useProfitability` option.
    #### `payoutAddress`
    : Possible values: any valid address for the `coin`. Your payout address of the specific coin of the upstream. Required for Foxy-Pools.
    #### `accountName`
    : Possible values: any string. Used to set a custom account name in Foxy-Pool to show instead of your `payoutAddress`.
    #### `minerName`
    : Possible values: any string. Used to set a custom miner name in Foxy-Pool to show when you click on your account in the miner list. If not specified the miner name supplied by scavenger is used, which is the hostname of the machine.
    #### `weight`
    : Possible values: any number. Defines how new blocks are queued. Blocks from upstreams with a higher weight interrupt currently scanning blocks of upstreams with a lower weight. Defaults to 10.
    #### `color`
    : Possible values: Any hex string, eg. `'#e2ad58'`. The color is used for the upstreams name in cli output.
    #### `distributionRatio`
    : Possible values: `n-m`, where `n` plus `m` must equal `100` in total. Used on Foxy-Pools to determine how you want to distribute rewards. Eg. `50-50` or `100-0`. Defaults to `0-100`. Read more on [DR](../foxy-pool/distribution-ratio.md).
    #### `doNotInterruptAbovePercent`
    : Possible values: any number from `0` to `100`. Used for completing scans on lower weight upstreams when the scan progress percentage is greater or equal to the value, even though a higher weight upstream has a new block.
    #### `url`
    : Possible values: any valid url. Only needed when mining to other pools using legacy http polling.
    #### `updateMiningInfoInterval`
    : Possible values: any number. Not used for Foxy-Pools. Defines the number of milliseconds to poll for new mining information from the legacy http polling upstream. Defaults to `1000`.
    #### `targetDL`
    : Possible values: any number. Submissions with deadlines above this number are ignored by Foxy-Miner and not sent to the upstream.
    #### `minWeight`
    : Possible values: any number. Discard all new blocks with a weight below this value for this upstream.
    #### `submitProbability`
    : Possible values: any number from `0` to `100`. Use 95 for 95% submit probability per round (based on capacity and netDiff)
    #### `disabled`
    : Possible values: `true`, `false`. Set to `true` to disable this upstream.

### `minerConfig`
: Holds the miner specific configuration options.
    #### `useHddDirectIo`
    : Possible values: `true`, `false`. Allows scavenger to read your plot files more efficiently.
    #### `cpuWorkers`
    : Possible values: any number. Defines how many plot files should be processed by your CPU in parallel. Set to `0` to disable CPU processing.
    #### `useCpuThreadPinning`
    : Possible values: `true`, `false`. Can improve performance when using CPU processing on multi CPU systems.
    #### `gpuPlatform`
    : Possible values: any valid opencl platform id. In combination with the `gpuDevice` this defines which GPU should be used for GPU processing.
    #### `gpuDevice`
    : Possible values: any valid opencl device id. In combination with the `gpuPlatform` this defines which GPU should be used for GPU processing.
    #### `gpuThreads`
    : Possible values: any number. Defines how many threads should be spawned on the GPU. Setting `useGpuAsyncCompute` doubles this value. Most cards work best with 1 or 2 threads. Set to `0` to disable GPU processing.
    #### `gpuWorkers`
    : Possible values: any number. Defines how many plot files should be processed by your GPU in parallel.
    #### `gpuNoncesPerCache`
    : Possible values: any number. When running into a GPU processing bottleneck you can fine tune this number [like this](../configuring-scavenger.md#fine-tuning).
    #### `useGpuMemMapping`
    : Possible values: `true`, `false`. Can improve performance on integrated GPUs like Intel onboard graphics.
    #### `useGpuAsyncCompute`
    : Possible values: `true`, `false`. Improves performance on dedicated GPUs. Doubles your effective `gpuThreads`.
    #### `plotDirs`
    : A list of plot file directories to use for mining. For example:
    ```yaml
    plotDirs:
      - D:\
      - E:\
      - F:\
    ```

### `listenAddr`
: Possible values: any valid `<hostname/ip>:<port>`. Used for the underlying miner, like scavenger, to connect to.

### `isManaged`
: Possible values: `true`, `false`. When set to `true` Foxy-Miner will auto download the required miner binary if it does not exist and create or update the miner config file. Only scavenger is currently supported for auto management.

### `minerType`
: Possible values: `scavenger` or `conqueror`. Defines which underlying miner to use.

### `minerBinPath`
: Possible values: any valid path to a miner binary. The binary path of scavenger / conqueror when not using `isManaged`.

### `minerConfigPath`
: Possible values: any valid path to a miner config file. The custom miner config path for scavenger / conqueror when not using `isManaged`.

### `noColors`
: Possible values: `true`, `false`. When set to `true` disables all colors.

### `useProfitability`
: Possible values: `true`, `false`. When set to `true` uses dynamic weights based on profitabilities of the coins.

### `maxNumberOfChains`
: Possible values: any number. Set the max number of chains that should be scanning. Can be combined with `useProfitability` to only mine the `n` most profitable chains.

### `assumeScannedAfter`
: Possible values: any number. Set to the number of seconds the miner should take at most to scan a round, forces a chain switch when exceeded. Useful for miners where sometimes drives drop out and no `finished` line is printed.

### `accountColors`
: Possible values: a `'<accountId>': '<hexCode>'` object. Uses the defined colors for their respective accountId (plotterId). Example:
```yaml
accountColors:
  '32507633737044403': '#a442f5'
  '38015127018237919': '#4bcefa'
```

### `dashboardLogLines`
: Possible values: any number. Defaults to `16`. Changes how many log lines should be displayed when using the cli dashboard via `--live` startup parameter.

### `useEcoBlockRewards`
: Possible values: `true`, `false`. When set to `true` uses eco block rewards for the `useProfitability` option.

### `hideScanProgress`
: Possible values: `true`, `false`. When set to `true` hides the miners scan progress. Useful for conqueror in combination with pm2.

### `minerOutputToConsole`
: Possible values: `true`, `false`. When set to `true` redirects all output of the miner directly to the console without processing/parsing it.

### `miner`
: A list of upstreams and their miner configs, used only for multi miner setups where you run multiple miner instances on the same machine. This can be useful when the scan time of your drives differs significantly.
    #### `upstreams`
    : See [upstreams](#upstreams)
    #### `minerBinPath`
    : See [minerBinPath](#minerbinpath)
    #### `minerConfigPath`
    : See [minerConfigPath](#minerconfigpath)
    #### `minerType`
    : See [minerType](#minertype)
    #### `minerColor`
    : Possible values: Any hex string, eg. `'#e2ad58'`. Set to a color to display for this miner in multi miner setups.
    #### `disabled`
    : Possible values: `true`, `false`. Set to `true` to disable this miner.
