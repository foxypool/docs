## Initial setup

??? question "Are compressed plots supported?"
    Yes, compressed plots are supported

??? question "I can't log in with my Launcher Id?"
    You can log in once your PlotNFT fully switched over to Foxy.

??? question "Can i have more than one Launcher Id for the same account?"
    No, these will be separate accounts.

??? question "Changing the payout address"
    To change your payout address please use the GUI's "Edit Payout Instructions" button. When using the CLI you can use `chia plotnft change_payout_instructions -l <your launcher id here> -a <your new payout address here>`. Alternatively you can also edit the chia `config.yaml` directly. In this case please change the `payout_instructions` for your Plot NFT to your desired payout address. The `payout_instructions` needs to be in puzzle hash form.

## EC

??? question "Why is my EC so low?"
    The pool uses a sliding windows over the last 24h of partials submitted by your farmer(s). As the EC is based on your submitted partials it will also take 24h to ramp up.

??? question "My EC is still far below my real capacity?"
    Please check your `debug.log` for any errors, generally something is not working correctly in your setup if the EC is very low.
