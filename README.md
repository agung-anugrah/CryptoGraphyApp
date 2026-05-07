
# 🔐 Cryptography App

A modern desktop cryptography application built with Python using CustomTkinter for the user interface and the Cryptography library for secure encryption algorithms.

This application supports:

- 🔒 AES Encryption & Decryption
- 🔑 RSA Encryption & Decryption
- 🖥️ Modern GUI
- 📂 Easy to Use


## ✨ Features


🔒 Symmetric Cryptography (AES)
- Encrypt plaintext using AES
- Decrypt encrypted ciphertext
- Fast and secure symmetric encryption

🔑 Asymmetric Cryptography (RSA)
- Generate RSA public & private keys
- Encrypt data using public key
- Decrypt data using private key

🎨 User Interface
- Modern desktop GUI
- Built with CustomTkinter
- Easy navigation between encryption pages


## 🖼️ Application Structure

### 🏠 Main Page

The application contains:

- Symmetric Encryption & Decryption
  - Uses AES algorithm

- Asymmetric Encryption & Decryption
  - Uses RSA algorithm
## 🛠️ Technologies Used

- Python
- CustomTkinter
- Cryptography Library
- AES Algorithm
- RSA Algorithm


## 📦 Required Libraries

Install the required dependencies before running the application.

Install using pip

    pip install customtkinter cryptography
## 📚 Imported Modules
    import customtkinter as ctk
    from cryptography.hazmat.primitives import padding as sym_padding
    from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
    from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
    from cryptography.hazmat.primitives import serialization, hashes
    import os
## ▶️ How to Run

Clone this repository

```bash
  git clone https://github.com/agung-anugrah/CryptoGraphyApp.git
```

Open the project folder

```bash
  cd CryptoGraphyApp
```

Install dependencies

```bash
  pip install customtkinter cryptography
```

Run the application

```bash
  python main.py
```


## 🔐 Encryption Algorithms
AES (Advanced Encryption Standard)

- Used for symmetric encryption where the same key is used for encryption and decryption.

RSA (Rivest–Shamir–Adleman)

- Used for asymmetric encryption with public and private key pairs.
## 📸 Screenshots

### 🏠 Main Menu
![Main Menu](https://raw.githubusercontent.com/agung-anugrah/CryptoGraphyApp/master/images/main-menu.png)

### 🔒 Symmetric Encryption
![Symmetric](https://raw.githubusercontent.com/agung-anugrah/CryptoGraphyApp/master/images/simetris-menu.png)

### 🔑 Asymmetric Encryption
![Asymmetric](https://raw.githubusercontent.com/agung-anugrah/CryptoGraphyApp/master/images/asimetris-menu.png)
## 📁 Project Structure
    cryptography-app/
    │
    ├── main.py
    ├── images/
    └── README.md
## 🧠 Learning Purpose
This project was created to learn:

- Cryptography concepts
- AES & RSA encryption
- GUI development using CustomTkinter
- Secure data handling in Python
## 👨‍💻 Author

Made with ❤️ using Python
## 📜 License

This project is open-source and available under the MIT License.