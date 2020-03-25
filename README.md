# Factom-Sim

[![Build Status](https://travis-ci.org/stackdump/factom-sim.svg?branch=master)](https://travis-ci.org/stackdump/factom-sim)

Python wrapper useful for testing (only simulation for now)
runs Factomd simulator and factom-walletd on standard ports

uses w/ 15 sec block time & in-memory DB

WARNING: use caution may overwrite config files in standard location
only use this on a development machine

## Example

Run factomd and factom-walled

```
python -m factom_sim.run
```
Hit ctl-c to quit


## Future

Long term will produce a factomd build that ships as a python package.

tracked: https://github.com/FactomProject/factomd/issues/973
