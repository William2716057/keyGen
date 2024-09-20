from cryptography.fernet import Fernet

#generate first key
single_key = Fernet.generate_key()

print("Single example key: ", single_key)

#list to demonstrate multiple keys
print("List of keys: ")
def keyGen():
    for i in range(20):
            key = Fernet.generate_key()
            print(key)
keyGen()

#convert single_key into binary format
input_key = single_key.decode()
def string_to_binary(input_key):
    binary_representation = ''.join(format(ord(char), '08b') for char in input_key)
    return binary_representation

binary_output = string_to_binary(input_key)
print(binary_output)