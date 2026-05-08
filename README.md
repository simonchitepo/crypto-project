# Cryptographic Tool Suite

A modular Python application that implements both **classic ciphers** (Caesar, Vigenère, One‑Time Pad) and **modern cryptographic algorithms** (SHA‑256 hashing, RSA asymmetric encryption and digital signatures). The project offers two interfaces:

- 🖥️ **Tkinter GUI** – standalone desktop application with tabs for each cipher, red/green encrypt/decrypt buttons, and real‑time input/output.
- 🌐 **REST API** (FastAPI) – test all endpoints via swagger UI (`/docs`) or `curl`/Postman.

## Features

- Caesar Cipher (customisable shift)
- Vigenère Cipher (customisable keyword)
- One‑Time Pad (hex key generation and XOR encryption)
- SHA‑256 message hashing
- RSA key generation, encryption, decryption, and digital signature verification
- Unit tests for every cipher
- Ready‑to‑run: `python main.py` (GUI) or `python main.py --api` (server)

## Technologies

Python, Tkinter, Cryptography (hazmat), FastAPI, Uvicorn, Pydantic, Unittest

## Getting Started

```bash
pip install -r requirements.txt
python main.py                # Launch GUI
# or
python main.py --api          # Start REST server
