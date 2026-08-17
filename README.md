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

## Security Controls

| Control ID | Category | Description | Implementation | Status |
|---|---|---|---|---|
| SC-01 | Cryptographic Implementation | Modern algorithm correctness | SHA-256 hashing and RSA implemented via vetted libraries | Implemented |
| SC-02 | Educational Boundary | Classic ciphers clearly marked non-secure | README/docs flag Caesar/Vigenere/OTP as educational only | Implemented |
| SC-03 | API Security | Protect FastAPI endpoints | Input validation + rate limiting on REST API | Planned |
| SC-04 | Key Management | RSA key handling | Keys generated/stored with appropriate permissions, never logged | In progress |
| SC-05 | Secrets Hygiene | No hardcoded secrets in repo | Secret scanning (e.g. Gitleaks) in CI | Planned |

## Risk Register

| Risk ID | Description | Likelihood | Impact | Mitigation | Status |
|---|---|---|---|---|---|
| RR-01 | User mistakes classic ciphers (Caesar/Vigenere/OTP) for production-grade security | High | Medium | Clear README warning; UI label marking them "educational only" | Open |
| RR-02 | RSA keys generated with insufficient key size or weak randomness | Low | High | Enforce minimum key size (2048+), use OS CSPRNG | Open |
| RR-03 | FastAPI endpoints exposed without auth/rate limiting in a public deployment | Medium | Medium | Add API key/auth + rate limiting before any public exposure | Open |
| RR-04 | Secrets (keys, test credentials) accidentally committed to repo | Low | High | Add Gitleaks/secret scanning to CI | Open |
