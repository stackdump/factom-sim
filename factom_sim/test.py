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
    """ Verify APIs of Factomd sim and wallet run properly """


    def setUp(self):
        """ open client connections """
        self.w = factom.FactomWalletd()
        self.f = factom.Factomd(
            host='http://127.0.0.1:8088',
            fct_address='FA2jK2HcLnRdS94dEcU27rF3meoJfpUcZPSinpb7AwQvPRY6RL1Q',
            ec_address='EC3Hu1W7uMHf7CtSva1cMyr5rXKsu7rVqQtkJCDHqEV9dgh5FjAj'
            # username='rpc_username',
            # password='rpc_password'
        )

    def tearDown(self):
        """ close client connections """
        self.w.session.close()
        self.f.session.close()

    def test_buy_ec(self):
        """ test buying entry credits """
        
        # use a funded coinbase address with a known secret key
        self.w.import_address("Fs3E9gV6DXsYzf7Fqx1fVBQPQXV695eP3k5XbmHEZVRLkMdD9qCK")
        self.w.import_address("Es3C7Ybmj8qoG1xZNrTm18EWKjW3BgvXQDFWZ1q1LvxxUBW5S5DL")

        r = self.f.entry_credit_rate()
        rate = r['rate']
        self.assertEqual(rate, 1000)

        r = self.w.fct_to_ec(self.f, 50 * rate, fct_address=self.f.fct_address, ec_address=self.f.ec_address)
        self.assertEqual(r['message'], 'Successfully submitted the transaction')


if __name__ == '__main__':
    unittest.main()
