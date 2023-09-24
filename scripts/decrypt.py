import sys
from cryptography.fernet import Fernet

# Function to decrypt a string based on a key
def decrypt(key, encrypted_text):
    cipher_suite = Fernet(key)
    text_bytes = cipher_suite.decrypt(encrypted_text)
    decrypted_text = text_bytes.decode('utf-8')
    return decrypted_text

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py 'text_encrypted' 'key'")
        sys.exit(1)

    text_encrypted = sys.argv[1].encode('utf-8')
    key = sys.argv[2].encode('utf-8')

    text = decrypt(key, text_encrypted)
    print("Text:", text)
