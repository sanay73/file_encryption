from encryptor import decrypt_file


def header():
    print("\n")
    print("┌────────────────────────────────────────────────────┐")
    print("│       🔓 SECURE FILE DECRYPTION TOOL               │")
    print("│                                                    │")
    print("│                                                    │")
    print("│                                              sanay │")
    print("├────────────────────────────────────────────────────┤")
    print("│                                                    │")
    print("│   MAIN MENU                                        │")
    print("│                                                    │")
    print("│   01  Decrypt File                                 │")
    print("│   02  Exit                                         │")
    print("│                                                    │")
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
            print("│  🔓 DECRYPT FILE                                   │")
            print("└────────────────────────────────────────────────────┘")

            decrypt_file()

            input("\n  Press Enter to return to menu...")

        elif choice == "2":

            print("\n  Secure File Decryption Tool Closed. ") 
            break

        else:

            print("\n  ❌ Invalid option.")
            input("  Press Enter to continue...")


if __name__ == "__main__":
    main()
