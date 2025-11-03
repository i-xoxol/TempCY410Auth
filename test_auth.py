import unittest
import os
import json
from user import User
from auth import hash_password, verify_password, create_new_user
from main import login_user

class TestAuth(unittest.TestCase):

    def setUp(self):
        """Set up a temporary users.json for testing."""
        self.test_users_file = "test_users.json"
        self.users = []
        # Create a dummy user for testing login
        self.test_user = create_new_user("testuser", "Test User", "password123", self.users)
        User.save_users(self.users, self.test_users_file)
        self.users = User.load_users(self.test_users_file)

    def tearDown(self):
        """Clean up the temporary users.json file."""
        if os.path.exists(self.test_users_file):
            os.remove(self.test_users_file)

    def test_unique_username(self):
        """Test that creating a user with an existing username fails."""
        # Attempt to create a user with the same username
        with self.assertRaises(ValueError):
            create_new_user("testuser", "Another User", "password456", self.users)

    def test_password_hashing_and_salting(self):
        """Test the password hashing and salting mechanism."""
        password = "secure_password"
        salt1, hash1 = hash_password(password)
        salt2, hash2 = hash_password(password)

        # Same password, different salts should produce different hashes
        self.assertNotEqual(hash1, hash2)

        # Same password, same salt should produce the same hash
        _, hash3 = hash_password(password, bytes.fromhex(salt1))
        self.assertEqual(hash1, hash3)

    def test_password_verification(self):
        """Test the password verification logic."""
        password = "password123"
        # Correct password
        self.assertTrue(verify_password(self.test_user.salt, self.test_user.hashed_password, password))
        # Incorrect password
        self.assertFalse(verify_password(self.test_user.salt, self.test_user.hashed_password, "wrongpassword"))

    def test_vague_error_on_login(self):
        """Test that login provides a vague error for both wrong username and wrong password."""
        # Incorrect username
        success, message = login_user("nonexistentuser", "somepassword", self.users)
        self.assertFalse(success)
        self.assertEqual(message, "Error: Invalid username or password.")

        # Incorrect password
        success, message = login_user("testuser", "wrongpassword", self.users)
        self.assertFalse(success)
        self.assertEqual(message, "Error: Invalid username or password.")

    def test_user_to_dict(self):
        """Test the to_dict method of the User class."""
        user_dict = self.test_user.to_dict()
        self.assertEqual(user_dict["username"], "testuser")
        self.assertEqual(user_dict["name"], "Test User")
        self.assertEqual(user_dict["salt"], self.test_user.salt)
        self.assertEqual(user_dict["hashed_password"], self.test_user.hashed_password)

    def test_user_from_dict(self):
        """Test the from_dict method of the User class."""
        user_dict = self.test_user.to_dict()
        new_user = User.from_dict(user_dict)
        self.assertEqual(new_user.username, "testuser")
        self.assertEqual(new_user.name, "Test User")
        self.assertEqual(new_user.salt, self.test_user.salt)
        self.assertEqual(new_user.hashed_password, self.test_user.hashed_password)

    def test_save_and_load_users(self):
        """Test saving and loading users to/from a file."""
        # The setUp method already saves a user. We load it and check if it's correct.
        loaded_users = User.load_users(self.test_users_file)
        self.assertEqual(len(loaded_users), 1)
        self.assertEqual(loaded_users[0].username, "testuser")

        # Add another user and save
        create_new_user("testuser2", "Test User 2", "password456", self.users)
        User.save_users(self.users, self.test_users_file)
        loaded_users = User.load_users(self.test_users_file)
        self.assertEqual(len(loaded_users), 2)
        self.assertEqual(loaded_users[1].username, "testuser2")

if __name__ == '__main__':
    unittest.main()
