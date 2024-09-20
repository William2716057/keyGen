from cryptography.fernet import Fernet

#key = Fernet.generate_key()
def keyGen():
    for i in range(20):
            key = Fernet.generate_key()
            print(key)
keyGen()