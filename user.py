import json
import os

class User:
    def __init__(self, username, name, salt, hashed_password):
        self.username = username
        self.name = name
        self.salt = salt
        self.hashed_password = hashed_password

    def to_dict(self):
        return {
            "username": self.username,
            "name": self.name,
            "salt": self.salt,
            "hashed_password": self.hashed_password
        }

    @classmethod
    def from_dict(cls, user_data):
        return cls(user_data["username"], user_data["name"], user_data["salt"], user_data["hashed_password"])

    @classmethod
    def find_by_username(cls, username):
        users = cls.load_users()
        for user in users:
            if user.username == username:
                return user
        return None

    @classmethod
    def load_users(cls, file_path="users.json"):
        if not os.path.exists(file_path):
            return []
        with open(file_path, "r") as f:
            users_data = json.load(f)
        return [cls.from_dict(user_data) for user_data in users_data]

    @staticmethod
    def save_users(users, file_path="users.json"):
        with open(file_path, "w") as f:
            json.dump([user.to_dict() for user in users], f, indent=4)
