## General

??? faq "What is DR"
    DR is short for Distribution-Ratio, a feature that allows users to choose the ratio of block winner - historical share they want to use. This works exactly the same as outlined [here](../../../../proof-of-capacity/foxy-pool/distribution-ratio.md) for PoC. **Note**: it is not yet possible to change the default DR of 0-100.

## Initial setup

??? faq "I can't log in with my Launcher Id?"
    You can log in once your PlotNFT fully switched over to Foxy.

??? faq "Can i have more than one Launcher Id for the same account?"
    No, these will be separate accounts.

## EC

??? faq "Why is my EC so low?"
    The pool uses a sliding windows over the last 24h of partials submitted by your farmer(s). As the EC is based on your submitted partials it will also take 24h to ramp up.

??? faq "My EC is still far below my real capacity?"
    Please check your `debug.log` for any errors, generally something is not working correctly in your setup if the EC is very low.
