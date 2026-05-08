def vigenere_cipher(text, key, mode='encrypt'):
    key = key.lower()
    key_length = len(key)
    result = []
    key_idx = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_idx % key_length]) - ord('a')
            if mode == 'decrypt':
                shift = -shift
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(new_char)
            key_idx += 1
        else:
            result.append(char)
    return ''.join(result)

def encrypt(plaintext, key):
    return vigenere_cipher(plaintext, key, 'encrypt')

def decrypt(ciphertext, key):
    return vigenere_cipher(ciphertext, key, 'decrypt')
