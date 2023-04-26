## Configuration Location

The Chia-Dashboard-Satellite config (`config.yaml`) is located in your home directory in the `.config/chia-dashboard-satellite` subdirectory. For example on Windows:

    C:\Users\<User>\.config\chia-dashboard-satellite\config.yaml

## Configuration Options

The config file currently consists of these config options:

### `chiaConfigDirectory`
: The chia base config directory. Defaults to `<HOMEDIR>/.chia/mainnet`

### `apiKey`
: The api key given by the [Chia-Dashboard](https://dashboard.chia.foxypool.io) when adding a new satellite.

### `chiaDaemonAddress`
: Possible values: `<address>:<port>`. Use the specified chia daemon address to connect to. Overrides the daemon address and port of the chia config if specified.

### `excludedServices`:
: Possible values in the array: `fullNode`, `wallet`, `farmer`, `harvester`, `plotter`. An array with services to exclude from stats, even when they are running.

### `chiaDashboardCoreUrl`:
: The url the satellite should connect to for stats updates, default is `https://chia-dashboard-api.foxypool.io`.

### `responseTimeSampleSize`:
: How many response times should be aggregated to calculate the average response time as well as the worst response time.

### `maximumFarmingInfos`:
: How many farming infos should be collected for the chart. Maximum value: 100.

### `updateMode`:
: How often the satellite should update the dashboard core api. Possible values: `slow`, `regular`, `fast`. Defaults to `regular`.

### `enableCompatibilityMode`:
: This setting results in the old data format being sent to the api. Possible values: `true`, `false`. Defaults to true if using any dashboard core api other than the default one.


## Configuration Example

```yaml
chiaConfigDirectory: /home/felix/.chia/mainnet
apiKey: f2d3a4ed-6480-4ae8-b130-06fd1845b440
excludedServices:
  - wallet
  - fullNode
chiaDashboardCoreUrl: https://eu.chiadashboard.com
```
