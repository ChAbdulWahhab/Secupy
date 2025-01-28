import bcrypt
import logging

class Hasher:
    @staticmethod
    def hash_password(password: str) -> bytes:
        try:
            salt = bcrypt.gensalt()
            return bcrypt.hashpw(password.encode(), salt)
        except Exception as e:
            logging.error(f"Password hashing failed: {e}")
            raise

    @staticmethod
    def verify_password(password: str, hashed_password: bytes) -> bool:
        try:
            return bcrypt.checkpw(password.encode(), hashed_password)
        except Exception as e:
            logging.error(f"Password verification failed: {e}")
            return False
