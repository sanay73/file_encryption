from encryptor import encrypt_file


def show_header():
    print(r"""
███████╗███╗   ██╗ ██████╗██████╗ ██╗   ██╗██████╗ ████████╗ ██████╗ ██████╗
██╔════╝████╗  ██║██╔════╝██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
█████╗  ██╔██╗ ██║██║     ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║   ██║██████╔╝
██╔══╝  ██║╚██╗██║██║     ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║   ██║██╔══██╗
███████╗██║ ╚████║╚██████╗██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║  ██║
╚══════╝╚═╝  ╚═══╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═╝
""")


def main():

    show_header()

    print("       🔐 SECURE FILE ENCRYPTION TOOL")
    print("       Cybersecurity Project")
    print("       Developer: SANAY")
    print()

    print("[1] 🔒 Encrypt File")
    print("[2] 🚪 Exit")

    choice = input("\nSelect option: ")

    if choice == "1":
        encrypt_file()

    elif choice == "2":
        print("Exiting...")

    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()
