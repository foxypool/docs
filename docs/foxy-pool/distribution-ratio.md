Foxy-Pools support a feature named DR - short for Distribution Ratio - which allows you to define how you want to split your rewards.
You can think of DR as a group of miners mining in their own mini pool, separate from miners in another DR group. Only pledge rewards are shared across DR groups.

Popular DR's used are `0-100` and `100-0`. With `0-100` the block winner gets no extra share, 100% of the miner block reward is split according to each miners historical share.
With `100-0` the block winner gets the whole miner share, other miners get nothing. This is basically solo mining.

The DR can be configured via the [Settings Tab](settings.md) or via headers sent by the mining software.
Foxy-Miner and Foxy-Proxy provide a `distributionRatio` config option for it.

Mining software needs to send the header `X-DistributionRatio` in their `submitNonce` requests. This header should be a string following the `n-m` syntax where `n` is the block winner share and `m` is the historical share.

