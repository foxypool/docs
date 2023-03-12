---
title: Chia Farming Gateway
---

Foxy-Pool hosts a Chia Farming Gateway (`node.chia.foxypool.io:18444`) for anyone to use, which can be used to farm without a local full node. [Foxy-Farmer](../foxy-farmer/index.md) already uses this under the hood.

- [x] NFT and OG plots are both supported!

!!! info "Note"
    If you can run a full node, you should!

## Using the gateway

Besides running [Foxy-Farmer](../foxy-farmer/index.md) you can also use the gateway with a vanilla chia-blockchain install, just edit its `config.yaml` so that your farmers `full_node_peer` points to the gateway:
```yaml
farmer:
  full_node_peer:
    host: node.chia.foxypool.io
    port: 18444
```

## Fee

- Farmers using the Gateway with plots currently farming on Foxy-Pool use the gateway for free.
- Farmers with plots not currently farming on Foxy-Pool will be charged with a 1% fee for using.

## Are my keys safe?

Yes, the farming happens on your machine, the locally running farmer still signs your blocks, same as when running a local full node. Your keys do not leave your machine.
