from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.hashes import SHA256
import logging

class AsymmetricEncryptor:
    def __init__(self):
        self.private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.public_key = self.private_key.public_key()

    def encrypt(self, message: str) -> bytes:
        try:
            return self.public_key.encrypt(
                message.encode(),
                padding.OAEP(mgf=padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
            )
        except Exception as e:
            logging.error(f"Asymmetric encryption failed: {e}")
            raise

    def decrypt(self, ciphertext: bytes) -> str:
        try:
            return self.private_key.decrypt(
                ciphertext,
                padding.OAEP(mgf=padding.MGF1(algorithm=SHA256()), algorithm=SHA256(), label=None)
            ).decode()
        except Exception as e:
            logging.error(f"Asymmetric decryption failed: {e}")
            raise ValueError("Decryption failed: Invalid key or ciphertext.") from e
