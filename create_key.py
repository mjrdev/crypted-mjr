from cryptography.fernet import Fernet

# Function to generate an encryption key
def generate_key():
    return Fernet.generate_key()

key = generate_key()

print("your key is: ", key)