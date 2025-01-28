import hmac
from hashlib import sha256
import logging

class SecureCommunicator:
    def __init__(self, secret_key: str):
        self.secret_key = secret_key.encode()

    def generate_signature(self, message: str) -> str:
        try:
            return hmac.new(self.secret_key, message.encode(), sha256).hexdigest()
        except Exception as e:
            logging.error(f"Signature generation failed: {e}")
            raise

    def verify_signature(self, message: str, signature: str) -> bool:
        try:
            return hmac.compare_digest(self.generate_signature(message), signature)
        except Exception as e:
            logging.error(f"Signature verification failed: {e}")
            return False
