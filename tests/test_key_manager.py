import unittest
from secupy.key_manager import KeyManager

class TestKeyManager(unittest.TestCase):
    def test_key_generation(self):
        password = "securePassword123"
        key, salt = KeyManager.generate_key(password)
        self.assertIsNotNone(key)
        self.assertIsNotNone(salt)
