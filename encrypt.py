from cryptography.fernet import Fernet

with open("key","rb") as keyfile:
    key = keyfile.read()

text = input("Yazı:")
encoded_text = text.encode()

fernet = Fernet(key)
encrypted = fernet.encrypt(encoded_text)

with open("encrypted","wb") as encrypted_file:
    encrypted_file.write(encrypted)