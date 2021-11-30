## Initial setup

??? faq "I can't log in with my Launcher Id?"
    You can log in once your PlotNFT fully switched over to Foxy.

??? faq "Can i have more than one Launcher Id for the same account?"
    No, these will be separate accounts.

??? faq "Changing the payout address"
    To change your payout address please use the GUI's "Edit Payout Instructions" button. When not using the GUI but editing the chives `config.yaml` directly please change the `payout_instructions` for your Plot NFT to your desired payout address. The `payout_instructions` needs to be in puzzle hash form.

## EC

??? faq "Why is my EC so low?"
    The pool uses a sliding windows over the last 24h of partials submitted by your farmer(s). As the EC is based on your submitted partials it will also take 24h to ramp up.

??? faq "My EC is still far below my real capacity?"
    Please check your `debug.log` for any errors, generally something is not working correctly in your setup if the EC is very low.
