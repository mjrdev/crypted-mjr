import random
import string
import argparse

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a random password.")
    parser.add_argument("length", type=int, help="Length of the password")
    args = parser.parse_args()

    random_password = generate_random_password(args.length)
    print("Generated password:", random_password)
