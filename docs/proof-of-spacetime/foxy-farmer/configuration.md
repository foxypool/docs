The Foxy-Farmer config (`foxy-farmer.yaml`) is located in the same directory where you executed the binary.

## Example configuration

An example configuration can look like this:
```yaml
enable_harvester: true
enable_og_pooling: true
farmer_reward_address: xch1063ymlv3saaxkh87h287nc3laelnxss0897xdw6g8zj6yvaa4elslg0xfa
harvester_num_threads: 30
listen_host: 127.0.0.1
log_level: INFO
plot_directories:
  - 'D:\plots'
  - 'E:\plots'
plot_refresh_interval_seconds: 900
pool_payout_address: xch1063ymlv3saaxkh87h287nc3laelnxss0897xdw6g8zj6yvaa4elslg0xfa
```

## Configuration Options

The config file currently consists of these config options:

### `enable_harvester`
: Whether to start a harvester instance as well, or only a farmer instance.

### `enable_og_pooling`
: Whether to enable OG pooling with Foxy-Pool for your OG plots.

### `farmer_reward_address`
: The Chia address you want your farmer rewards (0.25 XCH) credited to.

### `harvester_num_threads`:
: How many threads the harvester service should use to lookup challenges.

### `listen_host`:
: The host/ip to listen on, will set `self_hostname` in the chia config of foxy-farmer.

### `log_level`:
: The log level to use. Possible values: `DEBUG`, `INFO`, `WARNING`, `ERROR`

### `plot_directories`:
: The plot directories to use.

### `plot_refresh_interval_seconds`:
: How often the harvester should rescan for new/deleted plots in your `plot_directories`.

### `pool_payout_address`:
: The Chia address you want your pool rewards credited to. This will be used as `payout_instructions` for all PlotNFTs and if OG pooling is enabled as the payout address for the OG pool. 
