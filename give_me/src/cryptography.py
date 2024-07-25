from cryptography.fernet import Fernet


def generate_key():
    return Fernet.generate_key()


def load_key(file_path):
    return file_path.read_bytes()


def save_key(file_path, key):
    file_path.write_bytes(key)


def encrypt_password(key, password):
    fernet = Fernet(key)
    return fernet.encrypt(password.encode()).decode()


def decrypt_password(key, encrypted_password):
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password.encode()).decode()
