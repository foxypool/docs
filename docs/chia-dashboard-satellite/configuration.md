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


## Configuration Example

```yaml
chiaConfigDirectory: /home/felix/.chia/mainnet
apiKey: f2d3a4ed-6480-4ae8-b130-06fd1845b440
excludedServices:
  - wallet
  - fullNode
```
