Foxy-Pools support a feature named DR - short for Distribution Ratio - which allows you to define how you want to split your rewards.

Popular DR's used are `0-100` and `100-0`. With `0-100` the block winner gets no extra share, 100% of the miner block reward is split according to each miners historical share.
With `100-0` the block winner gets the whole miner share, other miners get nothing. This is basically solo mining. The DR can be any combination you want.

Each miners [EC](ec.md) is multiplied by the historical share part of the DR and the historical EC share is based on the resulting value compared to all other miners in the pool. When a block is won each miner receives its share based on their historical EC share and the block winners DR.

!!! example
    A miner has 100 TiB EC and uses a DR of 0-100. His relative EC will be `100 * (100 / 100) = 100`.

    A miner has 100 TiB EC and uses a DR of 50-50. His relative EC will be `100 * (50 / 100) = 50`.

    The historical share is based on each miners relative EC compared to all miners relative EC.

    When a block is won by a miner with a DR of 20-80, the block winner gets 20% of the miners block rewards and the remaining 80% are shared with all miners according to their historical EC share.

    In this example the miner with a DR of 0-100 will receive double the amount of the miner with a DR of 50-50 because his relative EC is twice as big.

The DR can be configured via the [Settings Tab](settings.md) or via headers sent by the mining software.
Foxy-Miner provides a `distributionRatio` config option for it.

Mining software needs to send the header `X-DistributionRatio` in their `submitNonce` requests. This header should be a string following the `n-m` syntax where `n` is the block winner share and `m` is the historical share.

