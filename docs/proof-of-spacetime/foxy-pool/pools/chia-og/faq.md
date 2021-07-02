??? faq "What does "OG" stand for?"
    OG is short for "Original Gangster". The "old" existing solo plots were dubbed OG plots, thus this is a OG pool.

??? faq "Can i farm solo with some of my plots and pool with the rest?"
    If the plots share the same pool public key no, otherwise yes.

??? faq "Can i farm on multiple pools with the same plots?"
    No, that is cheating and will be detected by the pool, which will result in your accrued collateral being distributed to all other farmers on the pool and your pool public key being banned.

??? faq "Can i solo farm other coins with the same plots?"
    Yes

??? faq "Can you lower the 1.75 XCH collateral?"
    No, 1.75 XCH is the pool reward portion when a block is won. As such the collateral needs to be at least this amount to be used effectively against cheaters.

??? faq "I am new, can i become a trusted member?"
    Unless a trusted member vouches for you, no

??? faq "Why is my EC so low?"
    The pool uses a sliding windows over the last 24h of partials submitted by your farmer(s). As the EC is based on your submitted partials it will also take 24h to ramp up.

??? faq "My EC is still far below my real capacity?"
    Please check your `debug.log` for any errors, generally something is not working correctly in your setup if the EC is very low.

??? faq "What is the advantage over HPool or core-pool etc?"
    These other pools use closed source client software, which has full access to your private keys. This does not mean that they currently exploit this, but the possibility exists. Foxy-Pool uses only open source client software.

    Additionally, these other pools do not use a collateral based system, so users cheating the pool by multi farming on other pools reduce your profit greatly on these pools.

??? faq "What is DR"
    DR is short for Distribution-Ratio, a feature that allows users to choose the ratio of block winner - historical share they want to use. This works exactly the same as outlined [here](../../../../proof-of-capacity/foxy-pool/distribution-ratio.md) for PoC. **Note**: it is not yet possible to change the default DR of 0-100.

??? faq "I changed my config.yaml, but the config was reset?"
    They are not gone, just re-arranged. The chia-blockchain software sorts the config keys alphabetically.

??? faq "I can't log in with my pool public key?"
    You can log in once you submitted your first partial to the pool. Check out the section on how to [verify your farmer is working correctly](getting-started.md#verify-your-farmer-is-working-correctly).

??? faq "Can i have more than one pool public key for the same account?"
    No, these will be separate accounts

??? faq "Can i leave the pool, claim my collateral and re-join?"
    No, if you leave the pool, there is no coming back.

??? faq "Can i transfer the collateral to the portable plots pool once it is available?"
    Yes

??? faq "Will the OG pool continue to work after the official pooling protocol is released?"
    Yes, this pool is here to stay

??? faq "How long does it take till I can access the "My Farmer" tab in the pool web ui after I have completed the setup?"
    Once the first partial/proof is being accepted by the pool. This also depends on how many plots you have, the duration can range from minutes to hours.

??? faq "Adding pool_url and pool_payout_address"
    Please ensure both `pool_url` and `pool_payout_address` are added into the farmer section and NOT full_node_peer section, it should be the same indentation as `full_node_peer`.
