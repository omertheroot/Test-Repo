from cryptography.fernet import Fernet

with open("key","rb") as key_file:
    key = key_file.read()

with open("encrypted","rb") as encrypted_file:
    encrypted = encrypted_file.read()


fernet = Fernet(key)
decrypted = fernet.decrypt(encrypted)

decoded = decrypted.decode()
print(f"'{decoded}'")