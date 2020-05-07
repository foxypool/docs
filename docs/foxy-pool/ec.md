EC, short for Effective Capacity, is a computed value based on deadlines received by the pool. It is intended to reflect the performance of your miner.

!!! example
    A miner has 100 TiB worth of plot files but reads them very slowly.
    His performance will suffer as he won't be able to finish reading his plots for every block and thus a potentially
    better deadline is never submitted to the pool as a new round already started. His EC will thus be lower than 100 TiB.

The EC is calculated by the pool over a given amount of past rounds of a miners submitted best deadlines of these rounds.
The amount of rounds used for this varies by pool, but it can be seen on each pools info page:
> PPLNS over the last 240 blocks (12 h)

!!! tip
    If you notice your EC is particularly low and you can't further optimize it, using a [DR](distribution-ratio.md)
    of `100-0` might be an alternative to not lose out on earnings. This will require you to have a substantial mining
    capacity to win blocks on a daily basis, depending on network difficulty.

### How the EC is calculated

The formula used to calculate the EC is as follows:

$$
EC = \frac{alpha(n) * blockTime * (n - 1)}{\sum_{i=0}^n (\frac{deadline}{netDiff})}
$$
where `n` is the number of submitted rounds and `alpha` is defined as follows:

$$
alpha(n) = 1 - \frac{r - n}{n} * \ln(\frac{r}{r - n})
$$

where `r` is the given maximum number of rounds used by the pool.