import time
import threading
from os import path
from ctypes import *

here = path.abspath(path.dirname(__file__))


class FactomWalletd(threading.Thread):

    def __init__(self, *args, **kwargs):
        self.factom_walletd = cdll.LoadLibrary(here + "/factom-walletd.so")
        self.factom_walletd.Serve.argtypes = []
        self.factom_walletd.Shutdown.argtypes = []
        super(FactomWalletd, self).__init__(*args, **kwargs)

    def run(self):
        self.factom_walletd.Serve()

    def join(self, *args, **kwargs):
        self.factom_walletd.Shutdown()
        super(FactomWalletd, self).join(*args, **kwargs)


class Factomd(threading.Thread):

    def __init__(self, *args, **kwargs):
        self.factomd = cdll.LoadLibrary(here + "/libfactomd.so")
        self.factomd.Serve.argtypes = []
        self.factomd.Shutdown.argtypes = []
        super(Factomd, self).__init__(*args, **kwargs)

    def run(self):
        self.factomd.Serve()

    def join(self, *args, **kwargs):
        self.factomd.Shutdown()
        super(Factomd, self).join(*args, **kwargs)
