import hashlib
import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def encrypt_word(word, seed_phrase):
    password = hashlib.sha256(seed_phrase.encode()).hexdigest().encode()
    salt = b'salt_'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256,
        iterations=100000,
        salt=salt,
        length=32,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)
    encrypted_word = f.encrypt(word.encode())

    return encrypted_word

word = "secret"
seed_phrase = "phraset"
encrypted_word = encrypt_word(word, seed_phrase)

print("Encrypted word:", encrypted_word)
