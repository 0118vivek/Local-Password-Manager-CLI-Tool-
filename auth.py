
#Master Password Handling
import bcrypt
import json
import getpass
import os

CONFIG_FILE = "config.json"

def setup_master_password():
    password = getpass.getpass("Set master password: ").encode()
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    with open(CONFIG_FILE, "w") as f:
        json.dump({"master_hash": hashed.decode()}, f)
    print("Master password set.")

def verify_master_password():
    if not os.path.exists(CONFIG_FILE):
        print("First time setup required.")
        setup_master_password()
        return True
    password = getpass.getpass("Enter master password: ").encode()
    with open(CONFIG_FILE) as f:
        data = json.load(f)
    stored_hash = data["master_hash"].encode()
    return bcrypt.checkpw(password, stored_hash)
