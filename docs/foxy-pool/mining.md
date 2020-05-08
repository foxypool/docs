You can mine on Foxy-Pools using various mining software and connection methods.

- A Socket.IO connection offers push support by keeping a constant connection to the server open, which can slightly improve the time for the miner to detect a new round started as well as reducing the load on the pool.

- HTTP Polling is the "classic" way of connecting to a Burst Wallet and thus was adopted by most mining pools. Miners poll for new mining info every x seconds.

### Socket.IO

- [Foxy-Miner](../foxy-miner/index.md), mini proxy which wraps Scavenger and provides multi-mining, [example config](../foxy-miner/configuration.md#configuration-example)
- [Foxy-Proxy](../foxy-proxy/index.md), multi mining proxy with a web ui, [example config](../foxy-proxy/configuration.md#configuration-example)

### HTTP Polling

- [quetzalcoatl/blagominer](https://github.com/quetzalcoatl/blagominer/releases), CPU only multi-miner with pause/resume support. [example config](../../assets/example/config/quetzalcoatl-blagominer/miner.conf)
- [Archon](http://archonproxy.info/download), A collision free, multi-chain proof of capacity mining proxy. [example config](../../assets/example/config/archon/archon.yaml)
