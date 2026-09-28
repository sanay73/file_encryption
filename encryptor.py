import os
import hashlib
import base64
import getpass

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


SALT_SIZE = 16
ITERATIONS = 600000


def create_key(password, salt):

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=ITERATIONS
    )

    return base64.urlsafe_b64encode(
        kdf.derive(password.encode())
    )


def encrypt_file():

    filename = input("Enter file to encrypt: ")

    if not os.path.isfile(filename):
        print("❌ File not found.")
        return

    password = getpass.getpass("Enter password: ")

    salt = os.urandom(SALT_SIZE)

    key = create_key(password, salt)

    cipher = Fernet(key)

    with open(filename, "rb") as file:
        data = file.read()

    encrypted = cipher.encrypt(data)

    output = filename + ".enc"

    with open(output, "wb") as file:
        file.write(salt)
        file.write(encrypted)

    print("✅ File encrypted successfully.")
    print("Encrypted file:", output)
    print("Exiting...")
    exit()

def decrypt_file():

    filename = input("Enter encrypted file: ")

    if not os.path.isfile(filename):
        print("❌ File not found.")
        return

    password = getpass.getpass("Enter password: ")

    with open(filename, "rb") as file:
        salt = file.read(SALT_SIZE)
        encrypted = file.read()

    try:

        key = create_key(password, salt)

        cipher = Fernet(key)

        decrypted = cipher.decrypt(encrypted)

    except Exception:

        print("❌ Decryption failed.")
        print("Incorrect password or damaged file.")
        return

    if filename.endswith(".enc"):
        output = filename[:-4]
    else:
        output = filename + ".decrypted"

    with open(output, "wb") as file:
        file.write(decrypted)

    print("✅ File decrypted successfully.")
    print("Decrypted file:", output)
    print("Exiting...")
    exit()

def calculate_hash():

    filename = input("Enter file: ")

    if not os.path.isfile(filename):
        print("❌ File not found.")
        return

    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:

        while True:

            data = file.read(1024 * 1024)

            if not data:
                break

            sha256.update(data)

    print("\nSHA-256:")
    print(sha256.hexdigest())


def main():


    print(r"""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")

    print("=" * 80)
    print("                      SECURE FILE ENCRYPTION TOOL")
    print("=" * 80)

    while True:

        print("\n1. Encrypt file")
        print("2. Decrypt file")
        print("3. Calculate SHA-256")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            encrypt_file()

        elif choice == "2":
            decrypt_file()

        elif choice == "3":
            calculate_hash()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("❌ Invalid option.")


if __name__ == "__main__":
    main()
