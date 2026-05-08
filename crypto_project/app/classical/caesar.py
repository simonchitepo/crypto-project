def caesar_cipher(text, shift, mode='encrypt'):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = shift if mode == 'encrypt' else -shift
            new_char = chr((ord(char) - base + offset) % 26 + base)
            result.append(new_char)
        else:
            result.append(char)
    return ''.join(result)

def encrypt(plaintext, shift):
    return caesar_cipher(plaintext, shift, 'encrypt')

def decrypt(ciphertext, shift):
    return caesar_cipher(ciphertext, shift, 'decrypt')
