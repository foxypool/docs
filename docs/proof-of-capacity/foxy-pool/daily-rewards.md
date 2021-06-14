Each Foxy-Pool shows a "Daily Reward" value on its Dashboard. This value is the equivalent of the averaged mining
rewards (excluding pledge rewards) per PiB of EC per day. The value is computed using the last 10 days of won blocks.

Additionally, the daily reward is also shown in USD / PiB, this value is based on the current exchange rate of the coin, if available.

### How is the daily reward computed exactly?

The following formula is used to calculate the daily rewards:


$$
dailyReward = \frac{\sum_{i=0}^n (\frac{minerReward * (1 - poolFee)}{poolCapacityInPib})}{days}
$$

where `n` is the amount of rounds won, `minerReward` is the miner reward of each won block, `poolCapacityInPib` is the pools capacity in PiB at the time the block was won and `days` is the amount of days (as a decimal) since the oldest block won.
