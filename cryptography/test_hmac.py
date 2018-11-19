from unittest import TestCase
import hashlib

from cryptography.hmac import hmac


class TestHmac(TestCase):
    def setUp(self):
        def md5(m):
            return hashlib.md5(m.encode("ascii")).hexdigest()

        def sha1(m):
            return hashlib.sha1(m.encode("ascii")).hexdigest()

        def sha256(m):
            return hashlib.sha256(m.encode("ascii")).hexdigest()

        self.md5 = (md5, hashlib.md5().block_size)
        self.sha1 = (sha1, hashlib.sha1().block_size)
        self.sha256 = (sha256, hashlib.sha256().block_size)

    def test_hmac(self):
        # self.assertEqual(
        #     "74e6f7298a9c2d168935f58c001bad88",
        #     hmac("", "", self.md5)
        # )
        # self.assertEqual(
        #     "fbdb1d1b18aa6c08324b7d64b71fb76370690e1d",
        #     hmac("", "", self.sha1)
        # )
        # self.assertEqual(
        #     "b613679a0814d9ec772f95d778c35fc5ff1697c493715653c6c712144292c5ad",
        #     hmac("", "", self.sha256)
        # )

        key = "key"
        m = "The quick brown fox jumps over the lazy dog"
        self.assertEqual(
            "80070713463e7749b90c2dc24911e275",
            hmac(key, m, self.md5)
        )
        self.assertEqual(
            "de7c9b85b8b78aa6bc8a7a36f70a90701c9db4d9",
            hmac(key,m, self.sha1)
        )
        self.assertEqual(
            "f7bc83f430538424b13298e6aa6fb143ef4d59a14946175997479dbc2d1a3cd8",
            hmac(key, m, self.sha256)
        )
