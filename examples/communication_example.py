from secupy import SecureCommunicator

communicator = SecureCommunicator("mysecretkey")
message = "This is a secure message."
signature = communicator.generate_signature(message)

print(f"Message: {message}")
print(f"Generated Signature: {signature}")
print(f"Signature Valid: {communicator.verify_signature(message, signature)}")
