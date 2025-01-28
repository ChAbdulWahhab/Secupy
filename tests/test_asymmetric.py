import unittest
from secupy.asymmetric import AsymmetricEncryptor

class TestAsymmetricEncryptor(unittest.TestCase):
    def test_asymmetric_encryption(self):
        asymmetric = AsymmetricEncryptor()
        message = "Confidential Message"
        encrypted = asymmetric.encrypt(message)
        decrypted = asymmetric.decrypt(encrypted)
        self.assertEqual(message, decrypted)
