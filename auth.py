import hashlib
import os
from user import User

def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # Generate a random 16-byte salt
    
    # Ensure salt is bytes for hashing
    if isinstance(salt, str):
        salt = salt.encode('utf-8')

    hashed_password = hashlib.pbkdf2_hmac(
        'sha256',          # Hashing algorithm
        password.encode('utf-8'),  # Convert password to bytes
        salt,              # Salt
        100000             # Number of iterations (adjust as needed)
    )
    return salt.hex(), hashed_password.hex() # Store salt and hash as hex strings

def verify_password(stored_salt, stored_password_hash, provided_password):
    salt = bytes.fromhex(stored_salt)
    _, hashed_provided_password = hash_password(provided_password, salt)
    return hashed_provided_password == stored_password_hash

def create_new_user(username, name, password, users):
    if any(u.username == username for u in users):
        raise ValueError("Username already exists")
    salt, hashed_password = hash_password(password)
    new_user = User(username, name, salt, hashed_password)
    users.append(new_user)
    User.save_users(users)
    return new_user
