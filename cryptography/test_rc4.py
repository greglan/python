from unittest import TestCase

from cryptography.rc4 import *


def hexstr_to_int_list(s):
    pass


class TestRc4(TestCase):
    def setUp(self):
        self.keystreams = {
            'Key': 'EB9F7781B734CA72A719',
            'Wiki': '6044DB6D41B7',
            'Secret': '04D46B053CA87B59'
        }

        self.ciphertexts = {
            'Plaintext': 'BBF316E8D940AF0AD3',
            'pedia': '1021BF0420',
            'Attack at dawn': '45A01F645FC35B383552544B9BF5'
        }

    def test_prga(self):
        for key in self.keystreams:
            S = ksa(key)
            keystream = prga(S, len(self.keystreams[key]))
            self.assertEqual(keystream, self.keystreams[keystream])


    def test_rc4(self):
        # TODO
        self.fail()
