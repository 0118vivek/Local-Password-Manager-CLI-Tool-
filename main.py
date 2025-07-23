#CLI Application

from auth import verify_master_password
from crypto_utils import derive_key, encrypt, decrypt
from db_handler import init_db, add_credential, get_credentials
from clipboard import copy_to_clipboard
import getpass

def main():
    if not verify_master_password():
        print("Access Denied.")
        return

    init_db()
    key = derive_key(getpass.getpass("Re-enter master password for encryption: "))

    while True:
        print("\n1. Add Credential\n2. View All\n3. Exit")
        choice = input("Select: ")
        if choice == '1':
            site = input("Site: ")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            enc_pwd = encrypt(password, key)
            add_credential(site, username, enc_pwd)
            print("Saved successfully.")
        elif choice == '2':
            creds = get_credentials()
            for site, user, enc_pwd in creds:
                pwd = decrypt(enc_pwd, key)
                print(f"{site} | {user} | {pwd}")
                copy_to_clipboard(pwd)
        else:
            break

if __name__ == "__main__":
    main()
