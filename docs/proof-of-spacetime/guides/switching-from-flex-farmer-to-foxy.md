!!! info
    This Guide describes how to farm without a local full node, using the Foxy Chia Farming Gateway or Gigahorse Farming Gateway. If you can run a full node you should, in that case just follow [this guide](../foxy-pool/pools/chia/getting-started.md) to get started.

<span style="font-weight: 200;font-size:1.25rem;">First select which type of plots you use:</span>

=== "Gigahorse compressed plots"

    <span style="font-weight: 200;font-size:1.15rem;">Next select whether you want to setup your Farmer manually or use [Foxy-Farmer](../foxy-farmer/index.md), which can do all the config and setup for you:</span>

    === "Foxy-Farmer"
        1. Install Foxy-Farmer, see [this page](../foxy-farmer/installing.md){ target=_blank } on the various install methods.
        2. Run Foxy-Farmer once to generate a `foxy-farmer.yaml` as well as the `.foxy-farmer` directory in your users home directory using the first run wizard. This will take care of importing your 24 word mnemonic, joining the pool as well as showing your pool login link.
        3. Open the login link and check out the Pools "My Farmer" tab!

    === "Manual setup"

        Our friends from SpaceFarmers already wrote a [complete guide](https://wiki.spacefarmers.io/poolinfo/migrating_from_flexpool#step-by-step_guide){target=_blank} on how to switch from using FlexFarmer with Gigahorse plots to a Gigahorse Farmer & Harvester setup which uses a remote full node. The Guide also works for Foxy, you just need to substitute
        ```
        ./chia.bin plotnft join -i <wallet_id> -u https://xch.spacefarmers.io
        ```
        with
        ```
        ./chia.bin plotnft join -i <wallet_id> -u https://farmer-chia.foxypool.io
        ```
        and
        ```yaml
        farmer:
          full_node_peer:
            host: community-node.spacefarmers.io
            port: 8445
        ```
        with
        ```yaml
        farmer:
          full_node_peers:
          - host: eu1.gh-farming-gateway.chia.foxypool.io
            port: 38445
          - host: eu3.gh-farming-gateway.chia.foxypool.io
            port: 38445
        ```

=== "Uncompressed & Bladebit compressed plots"

    1. Install Foxy-Farmer, see [this page](../foxy-farmer/installing.md){ target=_blank } on the various install methods.
    2. Run Foxy-Farmer once to generate a `foxy-farmer.yaml` as well as the `.foxy-farmer` directory in your users home directory using the first run wizard. This will take care of importing your 24 word mnemonic, joining the pool as well as showing your pool login link.
    3. Open the login link and check out the Pools "My Farmer" tab!
