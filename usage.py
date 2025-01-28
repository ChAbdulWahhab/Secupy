from secupy import Encryptor, Hasher, SecureCommunicator, AsymmetricEncryptor

# Encryptor - Encrypt and Decrypt Example
encryptor = Encryptor()
message = "Hello!"
encrypted = encryptor.encrypt(message)
decrypted = encryptor.decrypt(encrypted)

print("=== Encryptor ===")
print("Original Message:", message)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)
print("-" * 50)

# Hasher - Hash Password and Verify Example
hasher = Hasher()
password = "password123"
hashed_password = hasher.hash_password(password)
is_verified = hasher.verify_password(password, hashed_password)

print("=== Hasher ===")
print("Original Password:", password)
print("Hashed Password:", hashed_password)
print("Password Verified:", is_verified)
print("-" * 50)

# SecureCommunicator - Signature Generation and Verification Example
communicator = SecureCommunicator("mysecretkey")
signature = communicator.generate_signature("message")
is_signature_valid = communicator.verify_signature("message", signature)

print("=== SecureCommunicator ===")
print("Generated Signature:", signature)
print("Is Signature Valid for 'message':", is_signature_valid)
print("Is Signature Valid for 'wrong_message':", communicator.verify_signature("wrong_message", signature))
print("-" * 50)

# AsymmetricEncryptor - Encrypt and Decrypt Example
asymmetric = AsymmetricEncryptor()
asymmetric_encrypted = asymmetric.encrypt("Secure Message")
asymmetric_decrypted = asymmetric.decrypt(asymmetric_encrypted)

print("=== AsymmetricEncryptor ===")
print("Encrypted (Asymmetric):", asymmetric_encrypted)
print("Decrypted (Asymmetric):", asymmetric_decrypted)
print("-" * 50)
