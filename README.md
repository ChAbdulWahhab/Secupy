# Secupy Library

## Overview
**Secupy** is a Python-based library designed for secure encryption, hashing, communication, and asymmetric encryption operations. It helps developers integrate security features such as message signing, password hashing, encryption/decryption, and asymmetric encryption into their applications seamlessly. 

This library provides a simple and efficient way to handle various security tasks, making it ideal for use in applications that require data protection and secure communications.

---

## Modules

1. **Encryptor**: Symmetric Encryption and Decryption using the Fernet algorithm.
2. **Hasher**: Secure hashing of passwords using bcrypt.
3. **SecureCommunicator**: Message signing and verification using HMAC.
4. **AsymmetricEncryptor**: Asymmetric encryption and decryption using RSA.
5. **KeyManager**: Generates cryptographic keys using PBKDF2 with a given password.

---

## Installation

To install Secupy, simply clone the repository and install the required dependencies.

```bash
git clone https://github.com/ChAbdulWahhab/Secupy
cd secupy
pip install -r requirements.txt
```

---

## Usage

Below are examples of how to use each module in both **Flask** and **Django** applications.

---

### 1. **Encryptor**: Symmetric Encryption and Decryption

The **Encryptor** class uses the Fernet encryption method to encrypt and decrypt messages securely.

#### Flask Example:

```python
from flask import Flask, request, jsonify
from secupy import Encryptor

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    message = request.json.get('message')
    encryptor = Encryptor()
    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)
    return jsonify({"Encrypted": encrypted, "Decrypted": decrypted})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Django Example:

```python
from django.http import JsonResponse
from secupy import Encryptor

def encrypt_message(request):
    message = request.POST.get('message')
    encryptor = Encryptor()
    encrypted = encryptor.encrypt(message)
    decrypted = encryptor.decrypt(encrypted)
    return JsonResponse({"Encrypted": encrypted, "Decrypted": decrypted})
```

---

### 2. **Hasher**: Password Hashing and Verification

The **Hasher** class uses bcrypt for securely hashing and verifying passwords.

#### Flask Example:

```python
from flask import Flask, request, jsonify
from secupy import Hasher

app = Flask(__name__)

@app.route('/hash-password', methods=['POST'])
def hash_password():
    password = request.json.get('password')
    hasher = Hasher()
    hashed_password = hasher.hash_password(password)
    is_valid = hasher.verify_password(password, hashed_password)
    return jsonify({"Hashed Password": hashed_password, "Password Valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Django Example:

```python
from django.http import JsonResponse
from secupy import Hasher

def hash_password(request):
    password = request.POST.get('password')
    hasher = Hasher()
    hashed_password = hasher.hash_password(password)
    is_valid = hasher.verify_password(password, hashed_password)
    return JsonResponse({"Hashed Password": hashed_password, "Password Valid": is_valid})
```

---

### 3. **SecureCommunicator**: Message Signing and Verification

The **SecureCommunicator** class uses HMAC with SHA-256 to securely sign messages and verify their authenticity.

#### Flask Example:

```python
from flask import Flask, request, jsonify
from secupy import SecureCommunicator

app = Flask(__name__)

@app.route('/secure-message', methods=['POST'])
def secure_message():
    message = request.json.get('message')
    secret_key = "your_secret_key"
    communicator = SecureCommunicator(secret_key)
    signature = communicator.generate_signature(message)
    is_valid = communicator.verify_signature(message, signature)
    return jsonify({"Message": message, "Signature Valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Django Example:

```python
from django.http import JsonResponse
from secupy import SecureCommunicator

def secure_message(request):
    message = request.POST.get('message')
    secret_key = "your_secret_key"
    communicator = SecureCommunicator(secret_key)
    signature = communicator.generate_signature(message)
    is_valid = communicator.verify_signature(message, signature)
    return JsonResponse({"Message": message, "Signature Valid": is_valid})
```

---

### 4. **AsymmetricEncryptor**: Asymmetric Encryption and Decryption

The **AsymmetricEncryptor** class uses RSA for asymmetric encryption and decryption, allowing secure communication between two parties with private and public keys.

#### Flask Example:

```python
from flask import Flask, request, jsonify
from secupy import AsymmetricEncryptor

app = Flask(__name__)

@app.route('/asymmetric-encrypt', methods=['POST'])
def asymmetric_encrypt():
    message = request.json.get('message')
    asymmetric = AsymmetricEncryptor()
    encrypted_message = asymmetric.encrypt(message)
    decrypted_message = asymmetric.decrypt(encrypted_message)
    return jsonify({"Encrypted Message": encrypted_message, "Decrypted Message": decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Django Example:

```python
from django.http import JsonResponse
from secupy import AsymmetricEncryptor

def asymmetric_encrypt(request):
    message = request.POST.get('message')
    asymmetric = AsymmetricEncryptor()
    encrypted_message = asymmetric.encrypt(message)
    decrypted_message = asymmetric.decrypt(encrypted_message)
    return JsonResponse({"Encrypted Message": encrypted_message, "Decrypted Message": decrypted_message})
```

---

### 5. **KeyManager**: Key Generation for Encryption

The **KeyManager** class generates secure cryptographic keys using PBKDF2 with a password.

#### Flask Example:

```python
from flask import Flask, request, jsonify
from secupy import KeyManager

app = Flask(__name__)

@app.route('/generate-key', methods=['POST'])
def generate_key():
    password = request.json.get('password')
    key_manager = KeyManager()
    key, salt = key_manager.generate_key(password)
    return jsonify({"Generated Key": key, "Salt": salt})

if __name__ == '__main__':
    app.run(debug=True)
```

#### Django Example:

```python
from django.http import JsonResponse
from secupy import KeyManager

def generate_key(request):
    password = request.POST.get('password')
    key_manager = KeyManager()
    key, salt = key_manager.generate_key(password)
    return JsonResponse({"Generated Key": key, "Salt": salt})
```

---

## Key Features:
- **Encryption**: Secure message encryption and decryption with Fernet and RSA.
- **Password Hashing**: Secure password hashing using bcrypt.
- **Message Authentication**: HMAC-based signature generation and verification.
- **Key Management**: Generate cryptographic keys securely using PBKDF2.
- **Asymmetric Encryption**: RSA-based public and private key encryption.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Conclusion

The **Secupy** library provides a powerful set of tools for handling encryption, decryption, hashing, and secure communication tasks in your applications. Whether you're building a web application in **Flask** or **Django**, integrating these features will help secure sensitive data and ensure the integrity of your communications.

---

This README provides all necessary details for developers to understand and implement the **Secupy** library within Flask and Django projects. It should be clear and professional for any developer using this in production environments.