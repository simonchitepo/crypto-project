from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.classical import caesar, vigenere, otp
from app.modern import sha256_hash, rsa_crypto

app = FastAPI(title="Crypto API")

class CaesarRequest(BaseModel):
    text: str
    shift: int

class VigenereRequest(BaseModel):
    text: str
    key: str

class HashRequest(BaseModel):
    text: str

class RSAEncryptRequest(BaseModel):
    public_key: str
    plaintext: str

class RSADecryptRequest(BaseModel):
    private_key: str
    ciphertext: str

@app.post("/caesar/encrypt")
def encrypt_caesar(req: CaesarRequest):
    return {"ciphertext": caesar.encrypt(req.text, req.shift)}

@app.post("/caesar/decrypt")
def decrypt_caesar(req: CaesarRequest):
    return {"plaintext": caesar.decrypt(req.text, req.shift)}

@app.post("/vigenere/encrypt")
def encrypt_vigenere(req: VigenereRequest):
    return {"ciphertext": vigenere.encrypt(req.text, req.key)}

@app.post("/vigenere/decrypt")
def decrypt_vigenere(req: VigenereRequest):
    return {"plaintext": vigenere.decrypt(req.text, req.key)}

@app.post("/otp/encrypt")
def encrypt_otp(req: HashRequest):
    cipher_hex, key_hex = otp.encrypt(req.text)
    return {"ciphertext": cipher_hex, "key": key_hex}

@app.post("/otp/decrypt")
def decrypt_otp(ciphertext: str, key: str):
    try:
        plaintext = otp.decrypt(ciphertext, key)
        return {"plaintext": plaintext}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/sha256/hash")
def hash_text(req: HashRequest):
    return {"hash": sha256_hash.hash_text(req.text)}

@app.get("/rsa/generate_keys")
def generate_keys_rsa():
    priv, pub = rsa_crypto.generate_key_pair()
    return {"private_key": priv, "public_key": pub}

@app.post("/rsa/encrypt")
def encrypt_rsa(req: RSAEncryptRequest):
    try:
        ciphertext = rsa_crypto.encrypt(req.public_key, req.plaintext)
        return {"ciphertext": ciphertext}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/rsa/decrypt")
def decrypt_rsa(req: RSADecryptRequest):
    try:
        plaintext = rsa_crypto.decrypt(req.private_key, req.ciphertext)
        return {"plaintext": plaintext}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
