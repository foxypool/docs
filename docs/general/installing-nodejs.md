=== "Windows"

    1. Head over to [nodejs.org/en/download](https://nodejs.org/en/download/)
    2. Download the LTS Windows Installer file
    3. Execute the installer

=== "Linux & Mac OS X"

    1. Make sure you have `curl` installed:

            sudo apt update
            sudo apt install curl
    or for Mac OS X:

            brew install curl


    2. Install nvm:

            curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.35.2/install.sh | bash

    3. Add nvm to the PATH so we can use it right away without logging out and back in:

            export NVM_DIR="$HOME/.nvm"
            [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
            [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion


    4. Install node using nvm:

            nvm install --lts

