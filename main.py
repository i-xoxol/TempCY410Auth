from user import User
from auth import create_new_user, verify_password

def login_user(username, password, users):
    user_found = None
    for u in users:
        if u.username == username:
            user_found = u
            break

    if user_found and verify_password(user_found.salt, user_found.hashed_password, password):
        return True, f"Welcome, {user_found.name}! You are logged in."
    else:
        return False, "Error: Invalid username or password."

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

            try:
                create_new_user(username, name, password, users)
                print(f"User '{username}' created successfully!")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            print("\n--- Login ---")
            username = input("Enter username: ")
            password = input("Enter password: ")
            success, message = login_user(username, password, users)
            print(message)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
