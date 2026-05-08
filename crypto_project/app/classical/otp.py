import os

def generate_key(length):
    return os.urandom(length)

def xor_bytes(data, key):
    return bytes(a ^ b for a, b in zip(data, key))

def encrypt(plaintext):
    data = plaintext.encode('utf-8')
    key = generate_key(len(data))
    cipher = xor_bytes(data, key)
    return cipher.hex(), key.hex()

def decrypt(cipher_hex, key_hex):
    cipher = bytes.fromhex(cipher_hex)
    key = bytes.fromhex(key_hex)
    decrypted = xor_bytes(cipher, key)
    return decrypted.decode('utf-8')
