import unittest
from rotcipher import rotcipher


class TestRotCipher(unittest.TestCase):
    def test_rot_cipher_exist(self):
        rotcipher.get_encrypted_text("hello, world!", 13)

    def test_that_rot_cipher_returns_correct_text(self):
        actual = rotcipher.get_encrypted_text("Hello,World!", 13)
        expected = "Uryyb,Jbeyq!"
        self.assertEqual(actual, expected)
        actual = rotcipher.get_encrypted_text("welcome,123", 13)
        expected = "jrypbzr,123"
        self.assertEqual(actual, expected)
