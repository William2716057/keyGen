from cryptography.fernet import Fernet

single_key = Fernet.generate_key()

print("Single example key: ", single_key)

def keyGen():
    for i in range(20):
            key = Fernet.generate_key()
            print(key)
keyGen()