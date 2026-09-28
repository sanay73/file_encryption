from encryptor import encrypt_file


def header():
    print("\n")
    print("┌────────────────────────────────────────────────────┐")
    print("│  🔐  SECURE FILE ENCRYPTION TOOL                   │")
    print("│      CYBERSECURITY PROJECT                          │")
    print("│                                                    │")
    print("│      Developer : SANAY                             │")
    print("├────────────────────────────────────────────────────┤")
    print("│                                                    │")
    print("│   MAIN MENU                                        │")
    print("│                                                    │")
    print("│   01  Encrypt File                                 │")
    print("│   02  File Information                             │")
    print("│   03  Exit                                         │")
    print("│                                                    │")
    print("├────────────────────────────────────────────────────┤")
    print("│  ● SYSTEM STATUS : READY                           │")
    print("└────────────────────────────────────────────────────┘")


def main():

    while True:

        header()

        choice = input("\n  Select an option › ").strip()

        if choice == "1":

            print("\n┌────────────────────────────────────────────────────┐")
            print("│  🔒 ENCRYPT FILE                                   │")
            print("└────────────────────────────────────────────────────┘")

            encrypt_file()

            input("\n  Press Enter to return to menu...")

        elif choice == "2":

            print("\n  📄 FILE INFORMATION")
            print("  This feature can be added next.")

            input("\n  Press Enter to continue...")

        elif choice == "3":

            print("\n  Secure File Encryption Tool closed.")
            break

        else:

            print("\n  ❌ Invalid option.")
            input("  Press Enter to continue...")


if __name__ == "__main__":
    main()
