## General

??? question "What does "OG" stand for?"
    OG is short for "Original Gangster". The "old" existing solo plots were dubbed OG plots, thus this is a OG pool.

??? question "Will the OG pool continue to work after the official pooling protocol is released?"
    Yes, this pool is here to stay

## Multi-Farming

??? question "Can i farm my OG plots on Foxy and my portable plots somewhere else?"
    Yes

??? question "Can i farm solo with some of my plots and pool with the rest?"
    If the plots share the same pool public key no, otherwise yes.

??? question "Can i farm on multiple pools with the same plots?"
    No, that is cheating and will be detected by the pool, which will result in your accrued collateral being distributed to all other farmers on the pool and your pool public key being banned.

??? question "Can i solo farm other coins with the same plots?"
    Yes

## Initial setup

??? question "I changed my config.yaml, but the config was reset?"
    They are not gone, just re-arranged. The chives-blockchain software sorts the config keys alphabetically.

??? question "I can't log in with my pool public key?"
    You can log in once you submitted your first partial to the pool. Check out the section on how to [verify your farmer is working correctly](getting-started.md#verify-your-farmer-is-working-correctly).

??? question "Can i have more than one pool public key for the same account?"
    No, these will be separate accounts

## EC

??? question "Why is my EC so low?"
    The pool uses a sliding windows over the last 24h of partials submitted by your farmer(s). As the EC is based on your submitted partials it will also take 24h to ramp up.

??? question "My EC is still far below my real capacity?"
    Please check your `debug.log` for any errors, generally something is not working correctly in your setup if the EC is very low.

## Collateral

??? question "Can you lower the 78.75 XCC collateral?"
    No, 78.75 XCC is the pool reward portion when a block is won. As such the collateral needs to be at least this amount to be used effectively against cheaters.

??? question "I am new, can i become a trusted member?"
    Unless a trusted member vouches for you, no

??? question "Can i leave the pool, claim my collateral and re-join?"
    No, if you leave the pool, there is no coming back.

??? question "Can i transfer the collateral to the portable plots pool once it is available?"
    No, but you can leave the pool with your collateral once all OG plots have been replotted for NFT plots.
