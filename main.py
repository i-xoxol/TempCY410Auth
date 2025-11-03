from user import User
from auth import create_new_user, verify_password

def main():
    users = User.load_users()

    while True:
        print("\n--- Authentication Module ---")
        print("1. Create User")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- Create New User ---")
            username = input("Enter username: ")
            name = input("Enter full name: ")
            password = input("Enter password: ")

            # Check if username already exists
            if any(u.username == username for u in users):
                print("Error: Username already exists. Please choose a different username.")
            else:
                create_new_user(username, name, password, users)
                print(f"User '{username}' created successfully!")

        elif choice == '2':
            print("\n--- Login ---")
            username = input("Enter username: ")
            password = input("Enter password: ")

            user_found = None
            for u in users:
                if u.username == username:
                    user_found = u
                    break

            if user_found and verify_password(user_found.salt, user_found.hashed_password, password):
                print(f"Welcome, {user_found.name}! You are logged in.")
            else:
                print("Error: Invalid username or password.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
