# File By Debojyoti Ganguly
# Date: 10/09/2024

import hashlib
import rsa


class User:
    def __init__(self, username) -> None:
        self.username = username
        self.uuid = hashlib.sha256(username.encode()).hexdigest()       # Hashing the username to generate a unique identifier this is also the public key
        self.private_key, self.public_key = rsa.newkeys(512)            # Generating a public and private key pair
    
    def __str__(self) -> str:
        return f"User: {self.username}, UUID: {self.uuid}"
    
    def sign(self, message):
        return rsa.sign(message.encode(), self.private_key, 'SHA-256')
    
    def verify(self, message, signature):
        return rsa.verify(message.encode(), signature, self.public_key)
    
    def encrypt(self, message):
        return rsa.encrypt(message.encode(), self.public_key)
    
    def get_public_key(self):
        return self.public_key

    

