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

### `recursive_plot_scan`:
: Whether to scan the plot directories recursively or not. Will set `recursive_plot_scan` on the chia harvester config.

### `plot_nfts`:
: A list of PlotNFTs to farm with. Will set `pool_list` on the chia pool config.

### `parallel_decompressor_count`:
: The number of CPUs to be used for decompressing plots. If this is set to `0`, then harvesting of compressed plots will be disabled. For GPU harvesting, set this value to `1`. For CPU harvesting, set it to the number of CPUs you want to use for decompression (typically `1`). Will set `parallel_decompressor_count` on the chia harvester config.

### `decompressor_thread_count`:
: The number of CPU threads that will participate in decompressing plots. This number multiplied by `parallel_decompressor_count` needs to less than or equal to the total number of CPU cores. Will set `decompressor_thread_count` on the chia harvester config.

### `use_gpu_harvesting`:
: Set to `true` to enable harvesting with a GPU. Note that in order to use this setting, your harvester must have an NVIDIA GPU with CUDA capability 5.2 and up, with at least 8GB of vRAM. Will set `use_gpu_harvesting` on the chia harvester config.

### `gpu_index`:
: If your harvester has multiple GPUs, use this setting to choose which one to use. If your harvester only has one GPU, then leave this set to `0`. Will set `gpu_index` on the chia harvester config.

### `enforce_gpu_index`:
: Set to `true` if your harvester has more than one GPU and you want to use one other than the default of `0`. Will set `enforce_gpu_index` on the chia harvester config.

### `decompressor_timeout`:
: The number of seconds for your decompressor to time out. The default value of `20` is typically fine. Will set `decompressor_timeout` on the chia harvester config.

### `disable_cpu_affinity`:
: This should typically be `false`. When it is `false`, when using multiple CPU decompressors, each with multiple threads, the threads for each decompressor will be assigned to different physical CPUs. This prevents them for competing over compute time. If it is set to `true`, the threads for each decompressor will be assigned to the same CPU. Will set `disable_cpu_affinity` on the chia harvester config.

### `max_compression_level_allowed`:
: The highest level of compression your harvester will support. In Chia version 2.0, the maximum level is `7`. This will likely be increased in the future, but for now, you cannot increase it beyond the default. You can, however, set it to a lower number if desired. Will set `max_compression_level_allowed` on the chia harvester config.
