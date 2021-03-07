[Scavenger](https://github.com/PoC-Consortium/scavenger) can be configured via the `config.yaml` config file. The following sane defaults can be used as a baseline for future fine tuning:

!!! info
    When using [Foxy-Miner](../foxy-miner/index.md) in managed mode (`isManaged`) please configure the corresponding values in the `foxy-miner.yaml` instead.

General:
```yaml
hdd_reader_thread_count: 0
hdd_use_direct_io: true
get_mining_info_interval: 500 # When mining to a local proxy or foxy-miner use a low value like 500
send_proxy_details: true
```

When CPU mining:
```yaml
cpu_threads: 0
cpu_worker_task_count: n # the number of drives configured
```

When mining with a dedicated GPU:
```yaml
gpu_threads: 2
gpu_worker_task_count: n # the number of drives configured
gpu_nonces_per_cache: 110592 # Or the default 262144 depending on the GPU
gpu_mem_mapping: false
gpu_async: true
```

When mining with a integrated GPU:
```yaml
gpu_threads: 1 # Or 2 if the iGPU is more powerful
gpu_worker_task_count: n # the number of drives configured
gpu_nonces_per_cache: 110592 # Or the default 262144 depending on the GPU
gpu_mem_mapping: true
gpu_async: false
```

## Fine-tuning
For fine-tuning please use the benchmark functionality of scavenger via
```yaml
benchmark_only: XPU
```
This will disable submitting deadlines found. Additionally you can add your plot file paths multiple times to increase the benchmark duration as well as maximize the file reading because of caching already read parts.
While in benchmark mode adjust the `cpu_threads` / `gpu_threads` and `gpu_nonces_per_cache` sizes depending on if you are CPU or GPU mining and observe the results to maximize speeds.


Use `scavenger -o` to print the opencl device list and the `ideal_nonce_cache_multiplier` for each opencl device to calculate the optimal `gpu_nonces_per_cache`:

```
19:53:39 [INFO]  OCL: platform 1, AMD Accelerated Parallel Processing - OpenCL 2.1 AMD-APP (2671.3)
19:53:39 [INFO]  OCL:   device 0, Advanced Micro Devices, Inc. - Tahiti
19:53:40 [INFO]  OCL:     cores=32,kernel_1_workgroupsize=256, kernel_2_workgroupsize=256
19:53:40 [INFO]  OCL:     ideal_nonce_cache_multiplier=8192
```

The `gpu_nonces_per_cache` should be a multiple of the `ideal_nonce_cache_multiplier` of the GPU used for scanning.

Furthermore you can use
```yaml
benchmark_only: IO
```
to verify how fast your drives are. This benchmark mode will effectively just read the plot files without any processing.
