=== "Using the binary"

      1. Download the latest binary zip for your OS from the [releases page](https://github.com/foxypool/foxy-farmer/releases/latest){target=_blank}
      2. Run the binary, it will create a default `foxy-farmer.yaml` in the current directory based on your current chia `config.yaml`. Note: if you never set up chia before you will need to import your 24 word mnemonic using `./foxy-farmer keys add`.
      3. Edit the `foxy-farmer.yaml` to your liking and restart foxy-farmer
      4. Profit!

=== "Running from source"

      1. Clone the git repo and cd into it: 
      ```bash
      git clone https://github.com/foxypool/foxy-farmer && cd foxy-farmer
      ```
      2. Install the dependencies: 
      ```bash
      pip install .
      ```
      3. Run using `foxy-farmer`, it will create a default `foxy-farmer.yaml` in the current directory based on your current chia `config.yaml`. Note: if you never set up chia before you will need to import your 24 word mnemonic using `foxy-farmer keys add`.
      4. Edit the `foxy-farmer.yaml` to your liking and restart foxy-farmer
      5. Profit!

=== "Using docker"

      A docker image based on the provided [Dockerfile](https://github.com/foxypool/foxy-farmer/blob/main/Dockerfile){target=_blank} is available via
      ```
      ghcr.io/foxypool/foxy-farmer:latest
      ```
      For specific tags see [this list](https://github.com/foxypool/foxy-farmer/pkgs/container/foxy-farmer){target=_blank}.
      A [docker-compose.yaml](https://github.com/foxypool/foxy-farmer/blob/main/docker-compose.yaml){target=_blank} example is available as well, to get started.

      Currently, this requires you to have a working `foxy-farmer.yaml` already available to mount into the container. See this [example configuration](configuration.md#example-configuration) for reference.
