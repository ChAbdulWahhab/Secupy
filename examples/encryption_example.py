from secupy import Encryptor

encryptor = Encryptor()
message = "Sensitive Data"
encrypted = encryptor.encrypt(message)
decrypted = encryptor.decrypt(encrypted)

print(f"Original: {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
