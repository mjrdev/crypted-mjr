import sys
from cryptography.fernet import Fernet

# Function to generate an encryption key
def generate_key():
    return Fernet.generate_key()

# Function to encrypt a string based on a key
def encrypt(key, text):
    cipher_suite = Fernet(key)
    text_bytes = text.encode('utf-8')
    encrypted_text = cipher_suite.encrypt(text_bytes)
    return encrypted_text

# Function to decrypt a string based on a key
def decrypt(key, encrypted_text):
    cipher_suite = Fernet(key)
    text_bytes = cipher_suite.decrypt(encrypted_text)
    decrypted_text = text_bytes.decode('utf-8')
    return decrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py 'text_to_encrypt'")
        sys.exit(1)

    key = b'tpppRgl6_Os2-NqrGqEeG3QC2agmQHuVIJVpyz0M6sg='
    original_text = sys.argv[1]

    encrypted_text = encrypt(key, original_text)
    print("Encrypted text:", encrypted_text)

    decrypted_text = decrypt(key, encrypted_text)
    print("Decrypted text:", decrypted_text)
    print("Your key:", key)
