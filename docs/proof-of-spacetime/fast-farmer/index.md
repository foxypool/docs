---
title: Fast Farmer
---

[Fast Farmer](https://github.com/GalactechsLLC/dg_fast_farmer){target=_blank} is a 3rd-party lightweight farmer for the chia blockchain developed by evergreen and written in rust and works by connecting to a regular chia full node.

- [x] Fast Farmer is fully supported on Foxy-Pool!
- [x] NFT and OG plots are supported!
- [x] Bladebit compressed plots are supported!
- [x] Gigahorse plots are supported, please use [the binaries from here](https://github.com/evergreen-xch/ff_giga_bins){target=_blank}


Fast Farmer can be used without a local full node, by using the Foxy [Chia Farming Gateway](../chia-farming-gateway/index.md). To use it just edit your `fast_farmer.yaml`: 
```yaml
fullnode_ws_host: farming-gateway-chia.foxypool.io
fullnode_ws_port: 443
```

To initialize a new setup completely without a local full node run:
=== "Windows"
    ```ps
    .\ff.exe init `
      --fullnode-rpc-host node-rpc-gateway-chia.foxypool.io `
      --fullnode-rpc-port 443 `
      --fullnode-ws-host farming-gateway-chia.foxypool.io `
      --fullnode-ws-port 443 `
      --payout-address <your xch address here> `
      -d <your plot directory here> `
      -d <your other plot directory here>
    ```

=== "Linux"
    ```bash
    ./ff init \
      --fullnode-rpc-host node-rpc-gateway-chia.foxypool.io \
      --fullnode-rpc-port 443 \
      --fullnode-ws-host farming-gateway-chia.foxypool.io \
      --fullnode-ws-port 443 \
      --payout-address <your xch address here> \
      -d <your plot directory here> \
      -d <your other plot directory here>
    ```

!!! info "Note"
    If you can run a full node, you should!
