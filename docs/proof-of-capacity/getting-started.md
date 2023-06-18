### So you want to start PoC mining with your HDD?

#### Preparation

1. You need to create your first [Plot file](glossary.md#plot-file). The plot file is created using a Plotter, a piece of software which generates the [nonces](glossary.md#nonce) for the plot file using your CPU or preferably your GPU.
Recommended Plotter:
    - [Turbo Plotter](https://blackpawn.com/tp/) (Windows, Linux & Mac OS X - requires a GUI to run, easy to use)
    - [Engraver](https://github.com/PoC-Consortium/engraver/releases) (Windows & Linux - can run headless, for more advanced users)

    For this tutorial Turbo Plotter is used.

2. A Plot file contains a unique id, the [Plotter Id](glossary.md#plotter-id), also referred to as [Account Id](glossary.md#account-id). The Plotter Id is coin agnostic and can be bound to SIGNA. To obtain a Plotter Id use a SIGNA wallet.

=== "SIGNA wallet"

    Please visit either your own SIGNA wallet or an [online wallet](https://wallet1.burst-team.us:2083/index.html) you trust and click on "New? Create Your Account!":

    ![SIGNA wallet create account](../assets/img/getting-started/signa-wallet-create-account.png){: loading=lazy }

    A secret phrase is generated for you, please store it in a secure location and make a backup!

    !!! info
        This secret phrase is directly related to the Plotter Id, without the secret phrase the Plot files for this Plotter Id can not be used correctly for mining.

    Once you have the secret phrase backed up and confirmed, the SIGNA wallet dashboard is visible, where you can retrieve the Plotter Id by clicking on the SIGNA address in the top left corner and selecting "Copy Numeric Account ID":

    ![SIGNA wallet copy numeric id](../assets/img/getting-started/signa-wallet-copy-numeric-id.png){: loading=lazy }

#### Plotting

1. Paste your Plotter Id into Turbo Plotter and click "OK":
    ![Turbo Plotter enter plotter id](../assets/img/getting-started/tp-enter-plotter-id.png){: loading=lazy }

2. Now make sure to select your GPU for plotting, add your HDD to the "Target disk path" and ensure "Max file size" is as high as possible, keep everything else on default:
    ![Turbo Plotter plotting setup](../assets/img/getting-started/tp-plot-setup.png){: loading=lazy }

    !!! info
        Having more RAM can improve plotting speed dramatically.

3. Once you started the plotting you can observe its progress and estimated time till it is done plotting:
    ![Turbo Plotter plotting](../assets/img/getting-started/tp-plotting.png){: loading=lazy }

4. While the Plot file is plotting, you can bind your Plotter Id to the pools. You can follow the binding guide for [SIGNA](foxy-pool/binding/signa.md) to do so.
5. You'll also need a [miner](glossary.md#mining-software), a piece of software reading your Plot files each round and submitting [deadlines](glossary.md#deadline) it finds in your Plot file to the pool.
   There are a number of supported and recommended mining software's listed [here](foxy-pool/mining.md), but to get started using [Foxy-Miner](foxy-miner/index.md) is recommended.
6. Once the Plot file is done plotting, add its path to your miner's plot file list in it's configuration file and start mining!

    ![Foxy-Miner add plot path](../assets/img/getting-started/foxy-miner-config-add-plot-path.png){: loading=lazy }

7. To plot additional drives just repeat steps 2, 3 and 6 with the new drive paths
