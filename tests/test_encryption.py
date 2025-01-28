import unittest
from secupy.encryption import Encryptor

class TestEncryptor(unittest.TestCase):
    def test_encryption_decryption(self):
        encryptor = Encryptor()
        message = "Test Message"
        encrypted = encryptor.encrypt(message)
        decrypted = encryptor.decrypt(encrypted)
        self.assertEqual(message, decrypted)
