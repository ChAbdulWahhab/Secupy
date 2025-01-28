from secupy import Hasher

hasher = Hasher()
password = "securePassword123"
hashed_password = hasher.hash_password(password)

print(f"Original Password: {password}")
print(f"Hashed Password: {hashed_password}")
print(f"Password Verified: {hasher.verify_password(password, hashed_password)}")
