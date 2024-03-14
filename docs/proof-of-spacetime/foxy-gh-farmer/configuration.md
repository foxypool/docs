The Foxy-GH-Farmer config (`foxy-gh-farmer.yaml`) is located in the same directory where you executed the binary.

## Example configuration

An example configuration can look like this:
```yaml
enable_harvester: true
farmer_reward_address: xch1063ymlv3saaxkh87h287nc3laelnxss0897xdw6g8zj6yvaa4elslg0xfa
harvester_num_threads: 30
listen_host: 127.0.0.1
log_level: INFO
plot_directories:
  - 'D:\plots'
  - 'E:\plots'
plot_refresh_interval_seconds: 3600
pool_payout_address: xch1063ymlv3saaxkh87h287nc3laelnxss0897xdw6g8zj6yvaa4elslg0xfa
# environment config options below only for syntax demonstration purposes, apply as need with the values you require
recompute_hosts: [192.168.1.42]
recompute_connect_timeout: 2000
recompute_retry_interval: 100
chiapos_max_cores: 8
chiapos_max_cuda_devices: 1
chiapos_max_opencl_devices: 1
chiapos_max_gpu_devices: 3
chiapos_opencl_platform: 2
chiapos_min_gpu_log_entries: 21
cuda_visible_devices: '0,2'
```

## Configuration Options

All environment options for Gigahorse are exposed via the config, so you don't need to fiddle around with setting those anymore.

The config file currently consists of these config options:

### `enable_harvester`
: Whether to start a harvester instance as well, or only a farmer instance.

### `farmer_reward_address`
: The Chia address you want your farmer rewards (0.125 XCH) credited to.

### `harvester_num_threads`:
: How many threads the harvester service should use to lookup challenges.

### `listen_host`:
: The host/ip to listen on, will set `self_hostname` in the chia config of foxy-gh-farmer.

### `log_level`:
: The log level to use. Possible values: `DEBUG`, `INFO`, `WARNING`, `ERROR`

### `plot_directories`:
: The plot directories to use.

### `plot_refresh_interval_seconds`:
: How often the harvester should rescan for new/deleted plots in your `plot_directories`.

### `plot_refresh_batch_size`:
: How many plots the harvester should process at once during plot refresh/rescan. If unset the default value is `300`. Decreasing this value will lower the load on your HDDs during plot refresh but increase the time for initially loading them.

### `plot_refresh_batch_sleep_ms`:
: The number of milliseconds to wait between plot refresh batches. If unset the default value is `1`. Increasing this value will lower the load on your HDDs during plot refresh but increase the time for initially loading them.

### `pool_payout_address`:
: The Chia address you want your pool rewards credited to. This will be used as `payout_instructions` for all PlotNFTs. 

### `recursive_plot_scan`:
: Whether to scan the plot directories recursively or not. Will set `recursive_plot_scan` on the chia harvester config.

### `plot_nfts`:
: A list of PlotNFTs to farm with. Will set `pool_list` on the chia pool config.

### `recompute_hosts`:
: Set your recompute hosts to use here, an empty array won't use any recompute servers. Accepts an array of strings or a string.

### `recompute_connect_timeout`:
: Timeout in milliseconds for connecting to a recompute server (default = 2000). Remove or set to `null` to unset.

### `recompute_retry_interval`:
: Interval in seconds how often to retry using a previously failed recompute server (default = 100). Remove or set to `null` to unset.

### `chiapos_max_cores`:
: The maximum number of CPU/GPU threads to use. Remove or set to `null` to unset.

### `chiapos_max_cuda_devices`:
: The maximum number of CUDA devices to use (overrides `chiapos_max_gpu_devices`). Remove or set to `null` to unset.

### `chiapos_max_opencl_devices`:
: The maximum number of OpenCL devices to use (overrides `chiapos_max_gpu_devices`). Remove or set to `null` to unset.

### `chiapos_max_gpu_devices`:
: The maximum number of CUDA or OpenCL devices. Remove or set to `null` to unset.

### `chiapos_opencl_platform`:
: Select which OpenCL platform to use when there are multiple OpenCL platforms on the system. Remove or set to `null` to unset.

### `chiapos_min_gpu_log_entries`:
: The minimum work size for GPU, can be set to modify transition to GPU based on C level (default = 21). Remove or set to `null` to unset.

### `cuda_visible_devices`:
: Specify a list of CUDA devices to use. Remove or set to `null` to unset.

### `chia_daemon_port`:
: If unset defaults to `55470`. Can be used to run multiple instances of Foxy-Farmer. Will set `daemon_port` on the chia config.

### `chia_farmer_port`:
: If unset defaults to `28447`. Can be used to run multiple instances of Foxy-Farmer. Will set `farmer.port` on the chia config.

### `chia_farmer_rpc_port`:
: If unset defaults to `28559`. Can be used to run multiple instances of Foxy-Farmer. Will set `farmer.rpc_port` on the chia config.

### `chia_harvester_rpc_port`:
: If unset defaults to `28560`. Can be used to run multiple instances of Foxy-Farmer. Will set `harvester.rpc_port` on the chia config.

### `chia_wallet_rpc_port`:
: If unset defaults to `29256`. Can be used to run multiple instances of Foxy-Farmer. Will set `wallet.rpc_port` on the chia config.
