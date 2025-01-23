import unittest

import rot_cipher


class RotCipher(unittest.TestCase):
    def test_rot_cipher_exist(self):
        rot_cipher.def_get_encrypted_text("hello, World", "uryyb, Jbeyq")

