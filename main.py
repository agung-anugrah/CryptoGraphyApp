from textwrap import fill

import customtkinter as ctk
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asym_padding
from cryptography.hazmat.primitives import serialization, hashes
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Cryptographh App")
        self.geometry("300x300+800+200")

        self.columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=1)


        ctk.CTkLabel(self, text="Cryptography App").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


        ctk.CTkButton(self, text="Asimetris",command=self.asimetris).grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkButton(self, text="Simetris",command=self.simetris).grid(row=2, column=0, padx=10, pady=10, sticky="nsew")


    def simetris(self):
        simetris_app = Simetris()
        simetris_app.mainloop()
    def asimetris(self):
        asimetris_app = Asimetris()
        asimetris_app.mainloop()

class Asimetris(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Asimetris App")
        self.geometry("1500x1000+0+0")

        # bagi layar jadi 2 kolom
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)



        # ===== FRAME ENKRIPSI =====
        frame_encrypt = ctk.CTkFrame(self)
        frame_encrypt.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(frame_encrypt, text="ENKRIPSI").pack(pady=10)

        #  FRAME KHUSUS RADIO BUTTON
        frame_radio_encrypt = ctk.CTkFrame(frame_encrypt)
        frame_radio_encrypt.pack(pady=5, fill="x")

        ctk.CTkLabel(frame_radio_encrypt, text="panjang kunci").pack(padx=10, anchor="w")

        self.key_encrypt = ctk.StringVar(value="2048")

        for val in ["2048", "3072", "4096"]:
            ctk.CTkRadioButton(
                frame_radio_encrypt,
                text=val,
                variable=self.key_encrypt,
                value=val
            ).pack(side="left", padx=5, pady=10)

        # frame key publiic
        frame_key_public = ctk.CTkFrame(frame_encrypt)
        frame_key_public.pack(pady=5, fill="x")


        ctk.CTkButton(frame_key_public,text="Buat Key Public",command=self.generate_key).pack(pady=10,padx=10,fill="x")

        ctk.CTkLabel(frame_key_public,text="Key Public").pack(padx=10,anchor="w")

        self.public_key_entry =ctk.CTkTextbox(frame_key_public,height=100)
        self.public_key_entry.pack(fill="x", padx=10, pady=10)


        # Frame input Text
        frame_input_encrypt = ctk.CTkFrame(frame_encrypt)
        frame_input_encrypt.pack(pady=10, fill="x")

        ctk.CTkLabel(frame_input_encrypt, text="Text (plain text)").pack(padx=10, anchor="w")
        self.input_encrypt = ctk.CTkEntry(frame_input_encrypt)
        self.input_encrypt.pack(pady=10, padx=10, fill="x")

        # tombol
        ctk.CTkButton(frame_encrypt, text="Enkripsikan",command=self.encrypt).pack(pady=10, padx=10,fill="x")

        # fram output
        frame_output_encrypt = ctk.CTkFrame(frame_encrypt)
        frame_output_encrypt.pack(pady=10, fill="x")

        # label hasil
        ctk.CTkLabel(frame_output_encrypt, text="Hasil").pack(padx=10, anchor="w")

        # output
        ctk.CTkLabel(frame_output_encrypt, text="Text (chiper text)").pack(padx=10, pady=10, anchor="w")
        self.output_encrypt = ctk.CTkTextbox(frame_output_encrypt, height=100)
        self.output_encrypt.pack(pady=10, padx=10, fill="x")

        # key hasil
        ctk.CTkLabel(frame_output_encrypt, text="Key Private").pack(padx=10, pady=5, anchor="w")
        self.key_result = ctk.CTkTextbox(frame_output_encrypt,height=200)
        self.key_result.pack(pady=10, padx=10, fill="x")




        # ===== FRAME DEKRIPSI =====
        frame_decrypt = ctk.CTkFrame(self)
        frame_decrypt.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_decrypt, text="DEKRIPSI").pack(pady=10)

        # frame input
        frame_input_decrypt = ctk.CTkFrame(frame_decrypt)
        frame_input_decrypt.pack(pady=10, fill="x")

        # input text
        ctk.CTkLabel(frame_input_decrypt, text="Text (chiper text)").pack(padx=10, anchor="w")
        self.input_decrypt = ctk.CTkTextbox(frame_input_decrypt, height=100)
        self.input_decrypt.pack(pady=10, padx=10, fill="x")

        # input key
        ctk.CTkLabel(frame_input_decrypt, text="Key Private").pack(padx=10, pady=5, anchor="w")
        self.key_input = ctk.CTkTextbox(frame_input_decrypt)
        self.key_input.pack(pady=10, padx=10, fill="x")

        # button decrypt
        ctk.CTkButton(frame_decrypt, text="Dekripsikan",command=self.decrypt).pack(pady=10, fill="x", padx=10)

        # frame hasil
        frame_output_decrypt = ctk.CTkFrame(frame_decrypt)
        frame_output_decrypt.pack(pady=10, fill="x")
        ctk.CTkLabel(frame_output_decrypt, text="Hasil").pack(padx=10, anchor="w")

        # output
        ctk.CTkLabel(frame_output_decrypt, text="Text (plain text)").pack(padx=10, pady=10, anchor="w")
        self.output_decrypt = ctk.CTkTextbox(frame_output_decrypt, height=100)
        self.output_decrypt.pack(pady=10, padx=10, fill="x")

    def generate_key(self):
        size = int(self.key_encrypt.get())

        private_key, public_key = RSACipher.generate_keys(size)

        # simpan private key (jangan tampilkan dulu)
        self._private_key = private_key

        pub = RSACipher.serialize_public_key(public_key)

        self.public_key_entry.delete("1.0", "end")
        self.public_key_entry.insert("1.0", pub.decode())

        # kosongkan private key display
        self.key_result.delete("1.0", "end")


    def encrypt(self):
        try:
            text = self.input_encrypt.get().strip()
            pub_key_str = self.public_key_entry.get("1.0", "end").strip()

            public_key = RSACipher.load_public_key(pub_key_str)
            ciphertext = RSACipher.encrypt(text, public_key)

            self.output_encrypt.delete("1.0", "end")
            self.output_encrypt.insert("1.0", ciphertext.hex())

            # 🔥 tampilkan private key di sini
            if hasattr(self, "_private_key"):
                priv = RSACipher.serialize_private_key(self._private_key)

                self.key_result.delete("1.0", "end")
                self.key_result.insert("1.0", priv.decode())

        except:
            self.output_encrypt.delete("1.0", "end")
            self.output_encrypt.insert("1.0", "Gagal enkripsi")

    def decrypt(self):
        try:
            hex_text = self.input_decrypt.get("1.0", "end").strip()
            priv_key_str = self.key_input.get("1.0", "end").strip()

            private_key = RSACipher.load_private_key(priv_key_str)

            plaintext = RSACipher.decrypt(bytes.fromhex(hex_text), private_key)

            self.output_decrypt.delete("1.0", "end")
            self.output_decrypt.insert("1.0", plaintext)

        except:
            self.output_decrypt.delete("1.0", "end")
            self.output_decrypt.insert("1.0", "Gagal decrypt")

class RSACipher:

    @staticmethod
    def generate_keys(key_size=2048):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=key_size
        )

        public_key = private_key.public_key()

        return private_key, public_key

    @staticmethod
    def serialize_public_key(public_key):
        return public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

    @staticmethod
    def serialize_private_key(private_key):
        return private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )

    @staticmethod
    def load_public_key(pem_data: str):
        return serialization.load_pem_public_key(pem_data.encode())

    @staticmethod
    def load_private_key(pem_data: str):
        return serialization.load_pem_private_key(pem_data.encode(), password=None)

    @staticmethod
    def encrypt(plaintext: str, public_key):
        return public_key.encrypt(
            plaintext.encode(),
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def decrypt(ciphertext: bytes, private_key):
        return private_key.decrypt(
            ciphertext,
            asym_padding.OAEP(
                mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        ).decode()

class Simetris(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simetris App")
        self.geometry("1500x700+0+0")

        # bagi layar jadi 2 kolom
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)




        # ===== FRAME ENKRIPSI =====
        frame_encrypt = ctk.CTkFrame(self)
        frame_encrypt.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        ctk.CTkLabel(frame_encrypt, text="ENKRIPSI").pack(pady=10)


        #  FRAME KHUSUS RADIO BUTTON
        frame_radio_encrypt = ctk.CTkFrame(frame_encrypt)
        frame_radio_encrypt.pack(pady=5,fill="x")

        ctk.CTkLabel(frame_radio_encrypt, text="panjang kunci").pack(padx=10,anchor="w")

        self.key_encrypt = ctk.StringVar(value="16")

        for val in ["16", "32", "64"]:
            ctk.CTkRadioButton(
                frame_radio_encrypt,
                text=val,
                variable=self.key_encrypt,
                value=val
            ).pack(side="left", padx=5,pady=10)


        # Frame input Text
        frame_input_encrypt = ctk.CTkFrame(frame_encrypt)
        frame_input_encrypt.pack(pady=10,fill="x")

        ctk.CTkLabel(frame_input_encrypt,text="Text (plain text)").pack(padx=10,anchor="w")
        self.input_encrypt = ctk.CTkTextbox(frame_input_encrypt, height=100)
        self.input_encrypt.pack(pady=10, padx=10, fill="x")

        # tombol
        ctk.CTkButton(frame_encrypt, text="Enkripsikan", command=self.encrypt ).pack(pady=10,padx=10,anchor="w",fill="x")


        #fram output
        frame_output_encrypt = ctk.CTkFrame(frame_encrypt)
        frame_output_encrypt.pack(pady=10,fill="x")

        #label hasil
        ctk.CTkLabel(frame_output_encrypt, text="Hasil").pack(padx=10,anchor="w")

        # output
        ctk.CTkLabel(frame_output_encrypt, text="Text (chiper text)").pack(padx=10,pady=10,anchor="w")
        self.output_encrypt = ctk.CTkTextbox(frame_output_encrypt, height=100)
        self.output_encrypt.pack(pady=10, padx=10, fill="x")

        # key hasil
        ctk.CTkLabel(frame_output_encrypt, text="key").pack(padx=10,pady=5,anchor="w")
        self.key_result = ctk.CTkEntry(frame_output_encrypt)
        self.key_result.pack(pady=10, padx=10, fill="x")






        # ===== FRAME DEKRIPSI =====
        frame_decrypt = ctk.CTkFrame(self)
        frame_decrypt.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        ctk.CTkLabel(frame_decrypt, text="DEKRIPSI").pack(pady=10)


        # frame input
        frame_input_decrypt = ctk.CTkFrame(frame_decrypt)
        frame_input_decrypt.pack(pady=10,fill="x")

        # input text
        ctk.CTkLabel(frame_input_decrypt, text="Text (chiper text)").pack(padx=10,anchor="w")
        self.input_decrypt = ctk.CTkTextbox(frame_input_decrypt, height=100)
        self.input_decrypt.pack(pady=10, padx=10, fill="x")

        # input key
        ctk.CTkLabel(frame_input_decrypt, text="Key").pack(padx=10,pady=5,anchor="w")
        self.key_input = ctk.CTkEntry(frame_input_decrypt)
        self.key_input.pack(pady=10, padx=10, fill="x")


        # button decrypt
        ctk.CTkButton(frame_decrypt, text="Dekripsikan", command=self.decrypt).pack(pady=10,fill="x",padx=10)


        #frame hasil
        frame_output_decrypt = ctk.CTkFrame(frame_decrypt)
        frame_output_decrypt.pack(pady=10,fill="x")
        ctk.CTkLabel(frame_output_decrypt, text="Hasil").pack(padx=10,anchor="w")

        # output
        ctk.CTkLabel(frame_output_decrypt, text="Text (plain text)").pack(padx=10,pady=10,anchor="w")
        self.output_decrypt = ctk.CTkTextbox(frame_output_decrypt, height=100)
        self.output_decrypt.pack(pady=10, padx=10, fill="x")

    def encrypt(self):
        text = self.input_encrypt.get("1.0", "end").strip()
        size = self.key_encrypt.get()
        if not text:
            return
        key = AESCipher.generate_key(size)
        chipertext = AESCipher.encrypt(text, key)
        #text
        self.output_encrypt.delete("1.0", "end")
        self.output_encrypt.insert("1.0", chipertext.hex())
        #key
        self.key_result.delete("0", "end")
        self.key_result.insert(0,key.hex() )


    def decrypt(self):
        try:
            hex_text = self.input_decrypt.get("1.0", "end").strip()
            key_hex = self.key_input.get().strip()

            if not hex_text or not key_hex:
                return

            ciphertext = bytes.fromhex(hex_text)
            key = bytes.fromhex(key_hex)

            plaintext = AESCipher.decrypt(ciphertext, key)

            self.output_decrypt.delete("1.0", "end")
            self.output_decrypt.insert("1.0", plaintext)

        except Exception:
            self.output_decrypt.delete("1.0", "end")
            self.output_decrypt.insert("1.0", "Gagal decrypt")

class AESCipher:
    @staticmethod
    def generate_key(size):
        size = int(size)

        # mapping 64 → 32 byte (AES-256)
        if size == 64:
            size = 32

        if size not in [16, 24, 32]:
            raise ValueError("Key harus 16, 24, atau 32 byte")

        return os.urandom(size)

    @staticmethod
    def encrypt(plaintext: str, key: bytes) -> bytes:
        iv = os.urandom(16)

        padder = sym_padding.PKCS7(128).padder()
        padded = padder.update(plaintext.encode()) + padder.finalize()

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        encryptor = cipher.encryptor()

        ciphertext = encryptor.update(padded) + encryptor.finalize()

        return iv + ciphertext

    @staticmethod
    def decrypt(ciphertext: bytes, key: bytes) -> str:
        iv = ciphertext[:16]
        data = ciphertext[16:]

        cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
        decryptor = cipher.decryptor()

        padded = decryptor.update(data) + decryptor.finalize()

        unpadder = sym_padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(padded) + unpadder.finalize()

        return plaintext.decode()

app = App()
app.mainloop()