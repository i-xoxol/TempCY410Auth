# Gemini Workspace Context

## Project Overview

This project is an authentication module for the CY-410 lab. It is intended to be used as a teaching tool for students to learn about authentication and security. The project is under version control using Git, and the remote repository is located at https://github.com/i-xoxol/TempCY410Auth.git.

## Project Architecture

The authentication module is implemented in Python and follows these principles:

*   **User Database:** User data is stored in `users.json` as a text file containing JSON objects, one for each user.
*   **Backend:** Python is used for all backend logic.
*   **Cryptography:** Cryptographically secure functions (e.g., `os.urandom` for salt generation, `hashlib.pbkdf2_hmac` for hashing) are used for random number generation and password hashing.
*   **Password Storage:** Passwords are securely stored using salting and hashing.
*   **Interface:** A command-line interface (CLI) allows users to interact with the module.
*   **CLI Options:** The CLI provides options for "Login" and "Create User".
*   **User Attributes:** Each user has a `username`, `name`, and `hashed_password` (along with its `salt`).

The project is structured into the following files:

*   `user.py`: Defines the `User` class, responsible for representing user data and handling the loading/saving of users to `users.json`.
*   `auth.py`: Contains the core authentication logic, including functions for secure password hashing, salting, and verification, as well as creating new user entries.
*   `main.py`: The main entry point for the application, providing the command-line interface for user registration and login.
*   `users.json`: The JSON file serving as the persistent storage for user accounts.

## Building and Running

To run the authentication module:

1.  Ensure you have Python installed.
2.  Navigate to the project directory in your terminal.
3.  Run the `main.py` script:
    ```bash
    python main.py
    ```
4.  Follow the on-screen prompts to either create a new user or log in.

## Development Conventions

**TODO:** Add development conventions, such as coding style, testing practices, and contribution guidelines.