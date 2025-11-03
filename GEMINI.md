# Gemini Workspace Context

## Project Overview

This project is an authentication module for the CY-410 lab. It is intended to be used as a teaching tool for students to learn about authentication and security. The project is under version control using Git, and the remote repository is located at https://github.com/i-xoxol/TempCY410Auth.git.

## Project Architecture

The authentication module is implemented as a client-server application using Python and Flask for the backend, and HTML/JavaScript for the frontend.

### Backend

*   **Framework:** Flask, a lightweight Python web framework.
*   **API Endpoints:**
    *   `/api/register`: Handles new user registration.
    *   `/api/login`: Authenticates users and provides a JSON Web Token (JWT) for session management.
    *   `/api/profile`: A protected endpoint that requires a valid JWT to display user information.
*   **User Database:** User data is stored in `users.json` as a text file containing JSON objects, one for each user.
*   **Cryptography:** Cryptographically secure functions (e.g., `os.urandom` for salt generation, `hashlib.pbkdf2_hmac` for hashing) are used for random number generation and password hashing.
*   **Password Storage:** Passwords are securely stored using salting and hashing.

### Frontend

*   **HTML Pages:**
    *   `index.html`: A landing page with "Login" and "Register" options.
    *   `login.html`: A page with a login form.
    *   `register.html`: A page with a registration form.
    *   `profile.html`: A page to display the user's profile.
*   **JavaScript:** The frontend uses JavaScript to:
    *   Send user input to the backend API.
    *   Handle the responses from the server.
    *   Manage the user's session using JWTs stored in local storage.
    *   Navigate between pages.

### Project Structure

The project is structured into the following files and directories:

*   `server.py`: The main entry point for the application, containing the Flask server and API endpoints.
*   `user.py`: Defines the `User` class, responsible for representing user data and handling the loading/saving of users to `users.json`.
*   `auth.py`: Contains the core authentication logic, including functions for secure password hashing, salting, and verification.
*   `test_auth.py`: Contains unit tests for the authentication module.
*   `templates/`: A directory containing the HTML files for the frontend.
    *   `index.html`
    *   `login.html`
    *   `register.html`
    *   `profile.html`
*   `.gitignore`: Specifies files and directories to be ignored by Git (e.g., `__pycache__/`, `users.json`).

## Building and Running

To run the application:

1.  Ensure you have Python and Flask installed (`pip install Flask PyJWT`).
2.  Navigate to the project directory in your terminal.
3.  Run the `server.py` script:
    ```bash
    python server.py
    ```
4.  Open your web browser and go to `http://127.0.0.1:5000/` to use the application.

## Testing

The project includes a suite of unit tests in `test_auth.py` to ensure the correctness and security of the authentication module. The tests cover the following aspects:

*   **Unique Username:** Ensures that the system prevents the creation of users with duplicate usernames.
*   **Password Hashing and Salting:** Verifies that the password hashing and salting mechanism is working correctly.
*   **Password Verification:** Checks the password verification logic.
*   **Vague Error Messages:** Confirms that the login process provides a generic error message for both incorrect usernames and incorrect passwords, which helps prevent username enumeration attacks.
*   **User Data Handling:** Tests the conversion of `User` objects to and from dictionaries, and the saving and loading of user data.

To run the tests, execute the following command in your terminal:

```bash
python -m unittest test_auth.py
```

## Development Conventions

**TODO:** Add development conventions, such as coding style, testing practices, and contribution guidelines.