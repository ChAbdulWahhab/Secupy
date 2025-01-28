from secupy.key_manager import KeyManager

# Example password
password = "my_secure_password"

# Generate the key and salt
generated_key, salt = KeyManager.generate_key(password)

print(f"Generated Key: {generated_key}")
print(f"Salt: {salt}")
