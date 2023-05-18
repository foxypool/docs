#### Compressed plots
A plot file where some data is not stored on disk, but instead computed on the fly using your CPU or GPU. Different `c` sizes indicate the level of the compression, where higher numbers mean higher compression. Currently, there are two implementations: "Chia Official" using bladebit and madMAx using gigahorse. You can see [this comparison](https://xch.farm/compressed-plots/){target=_blank} for details.

#### Plot file
The file holding your stored hashes for farming. Plot files have varying sizes indicated by their `k` size, where higher `k` sizes mean bigger plot files. Each step roughly doubles the plot size. The minimum `k` size for CHIA mainnet is 32 which results in a ~101 GiB plot file.

#### PlotNFT
A PlotNFT is a special on-chain coin used to facilitate pooled farming with the option to switch pools. When creating plots they are assigned to an PlotNFT which in turn points at a pool or solo.

#### Wallet Seed
The wallet seed consists of 24 words which are used to generate all private keys your wallet uses. When you have access to someone's 24 words you control all their funds and [PlotNFTs](#plotnft)!
