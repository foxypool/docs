!!! info
    This Guide describes how to farm without a local full node, using the Foxy Chia Farming Gateway or Gigahorse Node. If you can run a full node you should, in that case just follow [this guide](../foxy-pool/pools/chia/getting-started.md) to get started.

<span style="font-weight: 200;font-size:1.25rem;">First select which type of plots you use:</span>

=== "Gigahorse compressed plots"
    Our friends from SpaceFarmers already wrote a complete guide on how to switch from using FlexFarmer with Gigahorse plots to a Gigahorse Farmer & Harvester setup which uses a remote full node [here](https://wiki.spacefarmers.io/poolinfo/migrating_from_flexpool#step-by-step_guide){target=_blank}. The Guide also works for Foxy, you just need to substitute
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
    You can just use [Foxy-Farmer](../foxy-farmer/index.md), to install it please follow the steps listed [here](../foxy-farmer/installing.md).
