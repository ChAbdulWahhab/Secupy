from secupy import AsymmetricEncryptor

asymmetric = AsymmetricEncryptor()
message = "Confidential Message"
encrypted = asymmetric.encrypt(message)
decrypted = asymmetric.decrypt(encrypted)

print(f"Original Message: {message}")
print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
