from cryptography.fernet import Fernet
import logging

class Encryptor:
    def __init__(self, key: bytes = None):
        self.key = key or Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt(self, message: str) -> bytes:
        try:
            return self.cipher.encrypt(message.encode())
        except Exception as e:
            logging.error(f"Encryption failed: {e}")
            raise

    def decrypt(self, encrypted_message: bytes) -> str:
        try:
            return self.cipher.decrypt(encrypted_message).decode()
        except Exception as e:
            logging.error(f"Decryption failed: {e}")
            raise ValueError("Decryption failed: Invalid key or ciphertext.") from e

    def get_key(self) -> bytes:
        return self.key
