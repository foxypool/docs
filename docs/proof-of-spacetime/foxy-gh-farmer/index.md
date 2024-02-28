---
title: Foxy-GH-Farmer
---

!!! warning
    Foxy-GH-Farmer is deprecated, please use [Foxy-Farmer](../foxy-farmer) with the `gigahorse` backend instead!

    Steps to migrate:

    - Rename `foxy-gh-farmer.yaml` to `foxy-farmer.yaml` and add `backend: gigahorse` to it
    - Rename `.foxy-gh-farmer` in your users home directory to `.foxy-farmer`
    - Start foxy-farmer in the same directory as the `foxy-farmer.yaml`

[Foxy-GH-Farmer](https://github.com/foxypool/foxy-gh-farmer){target=_blank} is a simplified Gigahorse farmer for the chia blockchain using the Foxy-Pool Gigahorse Farming Gateway to farm without a full node running on your machine.

!!! info "Note"
    If you can run a full node, you should!

Foxy-GH-Farmer is useful in the following scenarios:

- Your hardware does not support running a full node

If you are migrating from FlexFarmer please check out [this guide](../guides/switching-from-flex-farmer-to-foxy.md).
