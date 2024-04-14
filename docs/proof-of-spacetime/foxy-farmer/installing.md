=== "Using the binary"

      1. On Linux ensure you have `ocl-icd-libopencl1` installed when using the gigahorse backend
      2. Download the latest binary zip for your OS from the [releases page](https://github.com/foxypool/foxy-farmer/releases/latest){target=_blank} or if you can not access GitHub there is a [direct download](https://downloads.foxypool.io/chia/foxy-farmer/latest/){target=_blank} as well.
      3. Run the binary and follow the first run wizard, it will create a `foxy-farmer.yaml` in the current directory based on your inputs.

        !!! note
            You can join the pool at any time, just run `./foxy-farmer join-pool`. You can add `--fee` to supply a fee in case the mempool is full.

      4. (Optional) Edit the `foxy-farmer.yaml` to your liking and restart foxy-farmer
      5. Profit!

=== "Running from source"

      1. On Linux ensure you have `ocl-icd-libopencl1` installed when using the gigahorse backend
      2. Clone the git repo and cd into it: 
      ```bash
      git clone https://github.com/foxypool/foxy-farmer && cd foxy-farmer
      ```
      3. Create a venv:
      ```bash
      python3 -m venv venv
      ```
      4. Install the dependencies: 
      ```bash
      venv/bin/pip install .
      ```
      5. Run using `venv/bin/foxy-farmer` (or activate the venv using `source venv/bin/activate` and then just use `foxy-farmer`) and follow the first run wizard, it will create a `foxy-farmer.yaml` in the current directory based on your inputs.

        !!! note
            You can join the pool at any time, just run `foxy-farmer join-pool`. You can add `--fee` to supply a fee in case the mempool is full.

      6. (Optional) Edit the `foxy-farmer.yaml` to your liking and restart foxy-farmer
      7. Profit!

=== "Using docker"

      A docker image based on the provided [Dockerfile](https://github.com/foxypool/foxy-farmer/blob/main/Dockerfile){target=_blank} is available via
      ```
      ghcr.io/foxypool/foxy-farmer:latest
      ```
      and
      ```
      foxypool/foxy-farmer:latest
      ```
      For specific tags see [this list](https://github.com/foxypool/foxy-farmer/pkgs/container/foxy-farmer){target=_blank}.
      A [docker-compose.yaml](https://github.com/foxypool/foxy-farmer/blob/main/docker-compose.yaml){target=_blank} example is available as well, to get started.

      Currently, this requires you to have a working `foxy-farmer.yaml` already available to mount into the container. See this [example configuration](configuration.md#example-configuration) for reference.
      If you do not have a `.chia_keys` directory from a previous chia install, you can set the `CHIA_MNEMONIC` environment variable to your 24 words and it will create they keyring accordingly. Please unset it again once done.

      If you do not have the `plot_nfts` key in your `foxy-farmer.yaml` you can either copy its value from the `pool_list` in a working chia `config.yaml`, or run the `join-pool` command inside the container.

    !!! note
        To execute the `join-pool` command please first `exec` into the running container with
        ```bash
        docker exec -it <name of your container> bash
        ```
        Then you can run `foxy-farmer join-pool` inside the container.
