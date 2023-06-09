import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_key(encrObj):
    password = encrObj.password_provided.encode()  # Convert to type bytes
    salt = b'0mb4t'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    encrObj.key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once