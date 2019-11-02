import time
import unittest
from factom_sim import Factomd, FactomWalletd
import factom 

fnode = Factomd()
wallet = FactomWalletd()

BLKTIME = 15  # sec


def wait_blocks(i):
    time.sleep(i * BLKTIME)


def setUpModule():
    fnode.start()
    wallet.start()
    wait_blocks(1)


def tearDownModule():
    fnode.join()
    wallet.join()


class TestSim(unittest.TestCase):

    def test_buy_ec(self):
        """ trigger an error to check shutdown code """
        
        w = factom.FactomWalletd()
        f = factom.Factomd(
            host='http://127.0.0.1:8088',
            fct_address='FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q',
            ec_address='EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj'
            # username='rpc_username',
            # password='rpc_password'
        )

        r = f.entry_credit_rate()
        print("rate:", r)
        rate = r['rate']

        r = w.fct_to_ec(f, 50 * rate, fct_address=f.fct_address, ec_address=f.ec_address)
        print(r)


if __name__ == '__main__':
    unittest.main()
