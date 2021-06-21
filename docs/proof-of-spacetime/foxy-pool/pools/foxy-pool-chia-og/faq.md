#### What does "OG" stand for?

OG is short for "Original Gangster". The "old" existing solo plots were dubbed OG plots, thus this is a OG pool.

#### Can i farm solo with some of my plots and pool with the rest?

If the plots share the same pool public key no, otherwise yes.

#### Can i farm on multiple pools with the same plots?

No, that is cheating and will be detected by the pool, which will result in your accrued collateral being distributed to all other farmers on the pool and your pool public key being banned.

#### Can i solo farm other coins with the same plots?

Yes

#### Can you lower the 1.75 XCH collateral?

No, 1.75 XCH is the pool reward portion when a block is won. As such the collateral needs to be at least this amount to be used effectively against cheaters.

#### I am new, can i become a trusted member?

Unless a trusted member vouches for you, no

#### Why is my EC so low?

The pool uses a sliding windows over the last 24h of partials submitted by your farmer(s). As the EC is based on your submitted partials it will also take 24h to ramp up.

#### My EC is still far below my real capacity?

Please check your `debug.log` for any errors, generally something is not working correctly in your setup if the EC is very low.

#### What is the advantage over HPool or core-pool etc?

These other pools use closed source client software, which has full access to your private keys. This does not mean that they currently exploit this, but the possibility exists. Foxy-Pool uses only open source client software.

Additionally, these other pools do not use a collateral based system, so users cheating the pool by multi farming on other pools reduce your profit greatly on these pools.

#### What is DR

DR is short for Distribution-Ratio, a feature that allows users to choose the ratio of block winner - historical share they want to use. This works exactly the same as outlined [here](../../../../proof-of-capacity/foxy-pool/distribution-ratio.md) for PoC. **Note**: it is not yet possible to change the default DR of 0-100.

#### I changed my config.yaml, but the config was reset?

They are not gone, just re-arranged. The chia-blockchain software sorts the config keys alphabetically.

#### I can't log in with my pool public key?

You can log in once you submitted your first partial to the pool. Check out the section on how to [verify your farmer is working correctly](getting-started.md#verify-your-farmer-is-working-correctly).

#### Can i have more than one pool public key for the same account?

No, these will be separate accounts

#### Can i leave the pool, claim my collateral and re-join?

No, if you leave the pool, there is no coming back.

#### Can i transfer the collateral to the portable plots pool once it is available?

Yes

#### Will the OG pool continue to work after the official pooling protocol is released?

Yes, this pool is here to stay
