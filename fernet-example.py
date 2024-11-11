#This code snippet demonstrates the use of the cryptography library 
# to encrypt and decrypt a message using symmetric encryption with the Fernet algorithm.
#pip install cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"my deep dark secret")
pw = "JOULU"
token = f.encrypt(pw.encode('utf-8'))
print(token)

secret = f.decrypt(token)
print(secret)

#open file to write binary
with open('token-crypted.bin', 'wb') as file:
    file.write(token)