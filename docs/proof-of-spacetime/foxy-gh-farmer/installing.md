=== "Using the binary"

     1. On Linux ensure you have `libgomp1` as well as `ocl-icd-libopencl1` installed
     2. Download the latest binary zip for your OS from the [releases page](https://github.com/foxypool/foxy-gh-farmer/releases/latest){target=_blank}
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
      3. Install the dependencies: 
      ```bash
      pip install .
      ```
      4. Run using `foxy-gh-farmer`, it will create a default `foxy-gh-farmer.yaml` in the current directory based on your current chia `config.yaml` if available.

        !!! note
            If you never set up chia before on this machine you will need to import your 24 word mnemonic using `./foxy-gh-farmer keys add` and ensure the `config.yaml` in `<USER_HOME>/.foxy-gh-farmer/mainnet/config/` includes your PlotNFT in the pool list. This can be achieved by manually copying it from another `config.yaml` or running `./foxy-gh-farmer join-pool`.

      5. Edit the `foxy-gh-farmer.yaml` to your liking and restart foxy-gh-farmer
      6. Profit!

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
