import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256
import logging

class KeyManager:
    @staticmethod
    def generate_key(password: str, salt: bytes = os.urandom(16)) -> bytes:
        try:
            kdf = PBKDF2HMAC(algorithm=SHA256(), length=32, salt=salt, iterations=100000)
            return kdf.derive(password.encode()), salt
        except Exception as e:
            logging.error(f"Key generation failed: {e}")
            raise
