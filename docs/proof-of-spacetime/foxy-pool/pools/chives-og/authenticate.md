!!! info
    Authenticating allows you to change your name and increase the minimum payout as well as leaving and rejoining the pool.

From your [My Farmer](https://chives-og.foxypool.io/my-farmer){target=_blank} page on the pool you will see a green authentication button.

![og-authentication-button](../../../../assets/img/getting-started/auth-og-account-button.png){ loading=lazy }

Clicking it will open a modal with instructions on what to do next:

1. Change into the directory, where the `chives` binary is located at. When using a git install this is inside the `./activate`-ed repo directory. Otherwise, please use the following:

    === "Windows"
        Open a powershell window and enter the following command:
        ```PowerShell
        cd (Get-Item "$ENV:LOCALAPPDATA\chives-blockchain\app*\resources\app.asar.unpacked\daemon").fullname
        ```

    === "Mac OS"
        Open a terminal and enter the following command:
        ```zsh
        cd /Applications/Chives.app/Contents/Resources/app.asar.unpacked/daemon
        ```

    === "Linux"
        Open a terminal/bash and enter the following command:
        ```bash
        cd /usr/lib/chives-blockchain/resources/app.asar.unpacked/daemon
        ```

2. Next we need to obtain the fingerprint for the pool public key, by entering the following command into the shell:

    === "Windows"
        ```PowerShell
        .\chives keys show
        ```

    === "Linux & Mac OS"
        ```bash
        ./chives keys show
        ```

    !!! info
        If you have multiple keys please use the fingerprint for the key you used to create your OG plots with.

3. Now we need to sign the data from the modal with our keys, identified by the fingerprint from above. To do so you need to run the following command with both the data to sign and your fingerprint from above substituted:

    === "Windows"
        ```PowerShell
        .\chives keys sign -t "m/12381n/9699n/1n/0n" -d <the data to sign here> -f <your fingerprint here>
        ```

        ??? example
            ```PowerShell
            .\chives keys sign -t "m/12381n/9699n/1n/0n" -d 1632306148 -f 67890123456
            ```

    === "Linux & Mac OS"
        ```bash
        ./chives keys sign -t "m/12381n/9699n/1n/0n" -d <the data to sign here> -f <your fingerprint here>
        ```

        ??? example
            ```bash
            ./chives keys sign -t "m/12381n/9699n/1n/0n" -d 1632306148 -f 67890123456
            ```

    !!! info
        Please note that the data to sign shown in the modal is updated every time the modal is (re-) opened, as it reflects the current time in seconds.

4. Finally, copy the signature from above into the modal on the pool website. It is important that no excess whitespaces or line breaks are included.

    !!! example
        ```
        a3eca5d55bc139ece8764b827799f331e971c1d2d75b9617114065df4f0ebd18ee77b120157e8d21e5b41ac6f2ff0d7a0f94b1964715ff972cc85e0722e711924b1caa525437e3d03f6b8575b2fd9104a66bf386f62a9b5101cd9534cdb5e12b
        ```
