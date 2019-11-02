#!/usr/bin/env python
import signal
import sys
from factom_sim import Factomd, FactomWalletd

fnode = Factomd()
wallet = FactomWalletd()


def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    fnode.join()
    wallet.join()
    sys.exit(0)


# run factomd and factom-walletd
if __name__ == '__main__':
    fnode.start()
    wallet.start()

    signal.signal(signal.SIGINT, signal_handler)
    print('Press Ctrl+C')
    signal.pause()
