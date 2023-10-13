!!! info
    This Guide describes how to farm without a local full node, using the Foxy Chia Farming Gateway or Gigahorse Node. If you can run a full node you should, in that case just follow [this guide](../foxy-pool/pools/chia/getting-started.md) to get started.

<span style="font-weight: 200;font-size:1.25rem;">First select which type of plots you use:</span>

=== "Gigahorse compressed plots"

    <span style="font-weight: 200;font-size:1.15rem;">Next select whether you want to setup your Farmer manually or use [Foxy-GH-Farmer](../foxy-gh-farmer/index.md), which can do all the config and setup for you:</span>

    === "Foxy-GH-Farmer"
        1. Install Foxy-GH-Farmer, see [this page](../foxy-gh-farmer/installing.md){ target=_blank } on the various install methods.
        2. Run Foxy-GH-Farmer once to generate a `foxy-gh-farmer.yaml` as well as the `.foxy-gh-farmer` directory in your users home directory.
        3. Import your 24 word mnemonic using `./foxy-gh-farmer keys add`
        4. Join the pool by running `./foxy-gh-farmer join-pool`. This will spin up the wallet service, wait till its synced, join all PlotNFTs to the Foxy-Pool and shutdown the wallet service again once done. This process can take up to 30 minutes.
        5. Run Foxy-GH-Farmer and check out the Pools "My Farmer" tab!

    === "Manual setup"

        Our friends from SpaceFarmers already wrote a [complete guide](https://wiki.spacefarmers.io/poolinfo/migrating_from_flexpool#step-by-step_guide){target=_blank} on how to switch from using FlexFarmer with Gigahorse plots to a Gigahorse Farmer & Harvester setup which uses a remote full node. The Guide also works for Foxy, you just need to substitute
        ```
        ./chia.bin plotnft join -i <wallet_id> -u https://xch.spacefarmers.io
        ```
        with
        ```
        ./chia.bin plotnft join -i <wallet_id> -u https://farmer.chia.foxypool.io
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
          full_node_peer:
            host: gh-node.chia.foxypool.io
            port: 18445
        ```

=== "Uncompressed & Bladebit compressed plots"

    1. Install Foxy-Farmer, see [this page](../foxy-farmer/installing.md){ target=_blank } on the various install methods.
    2. Run Foxy-Farmer once to generate a `foxy-farmer.yaml` as well as the `.foxy-farmer` directory in your users home directory.
    3. Import your 24 word mnemonic using `./foxy-farmer keys add`
    4. Join the pool by running `./foxy-farmer join-pool`. This will spin up the wallet service, wait till its synced, join all PlotNFTs to the Foxy-Pool and shutdown the wallet service again once done. This process can take up to 30 minutes.
    5. Run Foxy-Farmer and check out the Pools "My Farmer" tab!
