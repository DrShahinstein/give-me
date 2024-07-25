import os
import getpass
import pyperclip
from pathlib import Path
from give_me.src.cryptography import generate_key, load_key, save_key, encrypt_password, decrypt_password
from give_me.src.fileops import load_passwords, save_passwords


JSON_FILE = "givemepasswords.json"
KEY_FILE = "key"


class PasswordManager:
    def __init__(self):
        if os.name == 'nt':
            config_dir = Path(os.getenv('APPDATA')) / "give_me"
        else:
            config_dir = Path.home() / ".config" / "give_me"

        config_dir.mkdir(parents=True, exist_ok=True)

        self.data_file = config_dir / JSON_FILE
        self.key_file  = config_dir / KEY_FILE

        if not self.key_file.exists():
            self.key = generate_key()
            save_key(self.key_file, self.key)
        else:
            self.key = load_key(self.key_file)

        self.passwords = self.load_passwords()

    def load_passwords(self):
        data = load_passwords(self.data_file)
        return {name: decrypt_password(self.key, pwd) for name, pwd in data.items()}

    def save_passwords(self):
        encrypted_data = {name: encrypt_password(self.key, pwd) for name, pwd in self.passwords.items()}
        save_passwords(self.data_file, encrypted_data)

    def create_password(self, password_name):
        while password_name in self.passwords:
            print(f"Password '{password_name}' already exists. Choose a different name.")
            password_name = input("Enter the name for your password: ")
        password = getpass.getpass("Password: ")
        self.passwords[password_name] = password
        self.save_passwords()
        print(f"{password_name} created successfully!")

    def edit_password(self, password_name):
        if password_name in self.passwords:
            new_password = getpass.getpass("Enter new password: ")
            self.passwords[password_name] = new_password
            self.save_passwords()
            print(f"{password_name} updated successfully!")
        else:
            print(f"Password '{password_name}' not found.")

    def list_passwords(self, no_private):
        if not self.passwords:
            print("No passwords available")
        else:
            for name, password in self.passwords.items():
                if no_private:
                    print(f"{name}: {password}")
                else:
                    print(f"{name}: {'*' * len(password)}")

    def remove_password(self, password_name):
        if password_name in self.passwords:
            del self.passwords[password_name]
            self.save_passwords()
            print(f"{password_name} removed successfully!")
        else:
            print(f"Password '{password_name}' not found.")

    def copy_password(self, password_name):
        if password_name in self.passwords:
            pyperclip.copy(self.passwords[password_name])
            print(f"{password_name} copied!")
        else:
            print(f"Password '{password_name}' not found.")
