import sys
from cryptography.fernet import Fernet

# Function to encrypt a string based on a key
def encrypt(key, text):
    cipher_suite = Fernet(key)
    text_bytes = text.encode('utf-8')
    encrypted_text = cipher_suite.encrypt(text_bytes)
    return encrypted_text

if __name__ == "__main__":
    # if len(sys.argv) != 3:
    #     print("Usage: python encrypt.py 'text_to_encrypt'")
    #     sys.exit(1)

    key = sys.argv[1]
    original_text = sys.argv[2]

    encrypted_text = encrypt(key, original_text)
    print("Encrypted text:", encrypted_text)