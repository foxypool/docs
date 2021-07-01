You can mine on Foxy-Pools using various mining software and connection methods.

- Socket.IO and Websocket connections offer push support by keeping a constant connection to the server open, which can slightly improve the time for the miner to detect a new round started as well as drastically reduce the load on the pool.

- HTTP Polling is the "classic" way of connecting to a Signa Wallet and thus was adopted by most mining pools. Miners poll for new mining info every x seconds. This connection method is considered legacy.

=== "Socket.IO"

    - [Foxy-Miner](../foxy-miner/index.md), mini proxy which wraps Scavenger and provides multi-mining, [example config](../foxy-miner/configuration.md#configuration-example)
    - [Foxy-Proxy](../foxy-proxy/index.md), multi mining proxy with a web ui, [example config](../foxy-proxy/configuration.md#configuration-example)

=== "Websocket"

    - [ddProxy](http://www.ddproxy.sg/index_en.html#download), an intelligent multi-mining proxy with support for many coins. [config templates](http://www.ddproxy.sg/index_en.html#template)

=== "HTTP Polling (legacy)"

    - [quetzalcoatl/blagominer](https://github.com/quetzalcoatl/blagominer/releases), CPU only multi-miner with pause/resume support. [example config](../../assets/example/config/quetzalcoatl-blagominer/miner.conf)

!!! info
    If you are new to mining please head over to the [Getting Started Guide](../getting-started.md) to learn how to setup mining with your HDDs!
