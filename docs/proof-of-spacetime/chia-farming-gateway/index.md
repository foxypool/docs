---
title: Chia Farming Gateway
---

Foxy-Pool hosts a Chia Farming Gateway (`farming-gateway.chia.foxypool.io:28444`) for anyone to use, which can be used to farm without a local full node. [Foxy-Farmer](../foxy-farmer/index.md) already uses this under the hood.

- [x] NFT and OG plots are both supported!
- [x] Bladebit compressed plots are supported!
- [x] Gigahorse compressed plots are supported when using [Fast Farmer](../fast-farmer)!
- [x] DrPlotter compressed plots are supported!

!!! info "Note"
    If you can run a full node, you should!

## Using the gateway

Besides running [Foxy-Farmer](../foxy-farmer/index.md) you can also use the gateway with a vanilla chia-blockchain install, just edit its `config.yaml` so that your farmers `full_node_peers` point to the gateway:
```yaml
farmer:
  full_node_peers:
  - host: dus1.farming-gateway.chia.foxypool.io
    port: 28444
  - host: nue1.farming-gateway.chia.foxypool.io
    port: 28444
```

## Fee

- Farmers using the Gateway with plots currently farming on Foxy-Pool use the gateway for free.
- Farmers with plots not currently farming on Foxy-Pool will be charged with a 1% fee for using.

## Are my keys safe?

Yes, the farming happens on your machine, the locally running farmer still signs your blocks, same as when running a local full node. Your keys do not leave your machine.
