=== "Using the binary"

     1. On Linux ensure you have `libgomp1` as well as `ocl-icd-libopencl1` installed
     2. Download the latest binary zip for your OS from the [releases page](https://github.com/foxypool/foxy-gh-farmer/releases/latest){target=_blank} or if you can not access GitHub there is a [direct download](https://downloads.foxypool.io/chia/foxy-gh-farmer/latest/){target=_blank} as well.
     3. Run the binary, it will create a default `foxy-gh-farmer.yaml` in the current directory based on your current chia `config.yaml` if available.

        !!! note
            If you never set up chia before on this machine you will need to import your 24 word mnemonic using `./foxy-gh-farmer keys add` and ensure the `config.yaml` in `<USER_HOME>/.foxy-gh-farmer/mainnet/config/` includes your PlotNFT in the pool list. This can be achieved by manually copying it from another `config.yaml` or running `./foxy-gh-farmer join-pool`.

     4. Edit the `foxy-gh-farmer.yaml` to your liking and restart foxy-gh-farmer
     5. Profit!

=== "Running from source"

      1. On Linux ensure you have `libgomp1` as well as `ocl-icd-libopencl1` installed
      2. Clone the git repo and cd into it: 
      ```bash
      git clone https://github.com/foxypool/foxy-gh-farmer && cd foxy-gh-farmer
      ```
      3. Create a venv:
      ```bash
      python3 -m venv venv
      ```
      4. Install the dependencies: 
      ```bash
      venv/bin/pip install .
      ```
      5. Run using `venv/bin/foxy-gh-farmer` (or activate the venv using `source venv/bin/activate` and then just use `foxy-gh-farmer`), it will create a default `foxy-gh-farmer.yaml` in the current directory based on your current chia `config.yaml` if available.

        !!! note
            If you never set up chia before on this machine you will need to import your 24 word mnemonic using `venv/bin/foxy-gh-farmer keys add` and ensure the `config.yaml` in `<USER_HOME>/.foxy-gh-farmer/mainnet/config/` includes your PlotNFT in the pool list. This can be achieved by manually copying it from another `config.yaml` or running `venv/bin/foxy-gh-farmer join-pool`.

      6. Edit the `foxy-gh-farmer.yaml` to your liking and restart foxy-gh-farmer
      7. Profit!

=== "Using docker"

      A docker image based on the provided [Dockerfile](https://github.com/foxypool/foxy-gh-farmer/blob/main/Dockerfile){target=_blank} is available via
      ```
      ghcr.io/foxypool/foxy-gh-farmer:latest
      ```
      and
      ```
      foxypool/foxy-gh-farmer:latest
      ```
      For specific tags see [this list](https://github.com/foxypool/foxy-gh-farmer/pkgs/container/foxy-gh-farmer){target=_blank}.
      A [docker-compose.yaml](https://github.com/foxypool/foxy-gh-farmer/blob/main/docker-compose.yaml){target=_blank} example is available as well, to get started.

      Currently, this requires you to have a working `foxy-gh-farmer.yaml` already available to mount into the container. See this [example configuration](configuration.md#example-configuration) for reference.
      If you do not have a `.chia_keys` directory from a previous chia install, you can set the `CHIA_MNEMONIC` environment variable to your 24 words and it will create they keyring accordingly. Please unset it again once done.

    !!! note
        To execute the `join-pool` command please first `exec` into the running container with
        ```bash
        docker exec -it <name of your container> bash
        ```
        Then you can run `foxy-gh-farmer join-pool` inside the container.
