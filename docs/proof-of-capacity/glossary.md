#### Account Id
The numeric representation of a SIGNA account address. It is a long number like 1234567890123567890123.

#### Base target
The base target is calculated from the last blocks and adjusts the difficulty for miners. The lower the base target, the harder it is for a miner to find a low [deadline](#deadline). It gets adjusted by the network in a way that the coin can have a stable block time on average.

#### Binding
The process of assigning a [plotter id](#plotter-id) / [account id](#account-id) to an address, generally a pool. In SIGNA bindings are called [Reward Assignments](#reward-assignment).

#### SIGNA Account
A SIGNA account consists of a passphrase, from which you can derive the SIGNA address (S-XXXX-XXXX-XXXX-XXXXX) and the [Account Id](#account-id) (1234567890123..).

#### Deadline
A deadline represents a duration in seconds. The lowest deadline wins the round once its duration expired (measured since the start of the current round).

#### Mining Software
The mining software scans your plot files and submits [deadlines](#deadline) to the pool or wallet when solo mining. Only a 4096th of your plot file contents is scanned each round.

#### Network Difficulty
Network Difficulty, or NetDiff in short, is a value that can be read as an estimate on the total amount of space in Terabytes dedicated to a coin. Since this is a value that changes with every block in relation to base target, it should be taken into an average over at least a day before considered to be somewhat accurate.

#### Nonce
When generating a [plot file](#plot-file), you generate something that is called nonces. Each nonce contains 256 KiB of data that can be used by miners to calculate [deadlines](#deadline). Each nonce will have its own individual number. This number can range between 0-18446744073709551615 (2<sup>64</sup>). The number is also used as a seed when creating the nonce. Because of this each nonce has its own unique set of data.

#### Plot file
The file holding your stored hashes for mining. It consists of [nonces](#nonce). When creating plot files you have to ensure to not reuse nonces (indicated by `start_nonce` and the `nonce_count` of the plot file) as the content of the plot file would be identical and does not earn additional rewards.

#### Plotter Id
An alternative name for the [account id](#account-id). The Plotter Id is the first number in a [plot file](#plot-file) name.

#### POC
Proof-of-Capacity, the consensus algorithm of HDD mining coins, like SIGNA, etc.

#### POC1
The old legacy plot file format of SIGNA, not used anymore.

#### POC2
The currently used plot file format of SIGNA. Adopted by other coins like BHD etc. File name format: `<plotter_id>_<start_nonce>_<nonce_count>`

#### Reward Assignment
The SIGNA terminology for a [binding](#binding).

#### Solo mining
Submitting deadlines to a wallet directly is called solo mining. With solo mining you don't share rewards with anyone else but also only receive rewards when you win a block.


