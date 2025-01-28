import unittest
from secupy.hashing import Hasher

class TestHasher(unittest.TestCase):
    def test_hashing(self):
        hasher = Hasher()
        password = "test_password"
        hashed = hasher.hash_password(password)
        self.assertTrue(hasher.verify_password(password, hashed))
