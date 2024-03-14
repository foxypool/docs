Foxy-Pools support a feature named DR - short for Distribution Ratio - which allows you to define how you want to split your rewards.

!!! tip "Important"
    DR only affects the pool reward portion of a block win (0.875 XCH), the farmer reward portion (0.125 XCH) is not touched

Popular DR's used are `0-100` and `100-0`. With `0-100` the block winner gets no extra share, 100% of the pool block reward is split according to each farmers historical shares based on partials submitted.
With `100-0` the block winner gets the whole pool block reward, other farmers get nothing. This is basically solo mining. The DR can be any combination you want.

Each farmers partial submission shares are multiplied by the historical ratio part of the DR. When a block is won each farmer receives their share based on their historical relative shares and the block winners DR.

!!! example
    Assume the pool block reward is 0.875 XCH and the pool fee is 1%

    The following farmers are in the pool:

    - Farmer `A` with `100,000` shares and a DR of 0-100 (the default), `100,000` relative shares.
    - Farmer `B` with `100,000` shares and a DR of 50-50, `50,000` relative shares.
    - Farmer `C` with `100,000` shares and a DR of 20-80, `80,000` relative shares.
    - Farmer `D` with `100,000` shares and a DR of 100-0, `0` relative shares.
    
    Assume farmer `C` wins a block. The total relative shares are `230,000`.

    The pool block reward minus pool fee is 0.875 * 0.99 = 0.86625

    Farmer `C` gets 20% of the reward for winning the block with a DR of 20-80, so 0.86625 * 0.2 = 0.17325

    The remainder (0.86625 - 0.17325 = 0.693) will be distributed between all farmers with historical relative shares.

    - Farmer `A` has 100% historical relative shares, as such his share of the 0.693 is 100,000 / 230,000 = 0.43478. He receives 0.3013043
    - Farmer `B` has 50% historical relative shares, as such his share of the 0.693 is 50,000 / 230,000 = 0.21739. He receives 0.15065217
    - Farmer `C` has 80% historical relative shares, as such his share of the 0.693 is 80,000 / 230,000 = 0.34783. He receives 0.24104347
    - Farmer `D` has 0% historical relative shares, as such his share of the 0.693 is 0. He receives 0

    If farmer `D` wins a block he gets the full 0.86625 and everyone else gets nothing.

The DR can be configured via rewards tab in the settings modal in the "My Farmer" tab.
