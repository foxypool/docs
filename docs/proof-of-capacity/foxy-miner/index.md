## What is Foxy-Miner

[Foxy-Miner](https://github.com/felixbrucker/foxy-miner) is a mini proxy which wraps [scavenger](https://github.com/PoC-Consortium/scavenger) or [conqueror](https://github.com/PoC-Consortium/Helix) to provide a few features these miners do not yet support themselves:

- Multi-Mining support, mine as many coins as you want with custom ordering of their priorities
- Scan the next chain as soon as the current scan is done
- Support Socket.IO based communication with Foxy-Pools or Foxy-Proxies for faster round starts and less network overhead
- Humanize deadlines, so you know exactly how low/big the deadlines are
- Add all sorts of configurable colors
- Support profitability based switching and exclusion of coins
- Help the user with a first run wizard through the setup process
