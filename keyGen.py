from cryptography.fernet import Fernet

single_key = Fernet.generate_key()

print("Single example key: ", single_key)
print("List of keys: ")
def keyGen():
    for i in range(20):
            key = Fernet.generate_key()
            print(key)
keyGen()