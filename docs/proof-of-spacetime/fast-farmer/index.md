---
title: Fast Farmer
---

[Fast Farmer](https://github.com/GalactechsLLC/dg_fast_farmer){target=_blank} is a 3rd-party lightweight farmer for the chia blockchain written in rust and works by connecting to a regular chia full node.

- [x] Fast Farmer is fully supported on Foxy-Pool!
- [x] NFT and OG plots are supported!
- [x] Bladebit compressed plots are supported!
- [ ] Gigahorse plots are not yet supported, but support is being worked on


Fast Farmer can be used without a local full node, by using the Foxy [Chia Farming Gateway](../chia-farming-gateway/index.md). To use it just edit your `fast_farmer.yaml`: 
```yaml
fullnode_ws_host: farming-gateway.chia.foxypool.io
fullnode_ws_port: 28444
```

To initialize a new setup completely without a local full node run:
```bash
./ff init \
  --fullnode-rpc-host node-rpc-gateway-chia.foxypool.io \
  --fullnode-rpc-port 443 \
  --fullnode-ws-host farming-gateway.chia.foxypool.io \
  --fullnode-ws-port 28444 \
  --mnemonic "<your 24 words here>" \
  --payout-address <your xch address here> \
  -d <your plot directory here> \
  -d <your other plot directory here>
```

!!! info "Note"
    If you can run a full node, you should!
