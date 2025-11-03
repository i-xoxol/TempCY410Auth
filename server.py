from flask import Flask, request, jsonify, render_template, redirect, url_for
import jwt
import datetime
from functools import wraps

from user import User
from auth import create_new_user, verify_password

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a random secret key

# --- Helper Functions ---

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = User.find_by_username(data['username'])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401

        return f(current_user, *args, **kwargs)

    return decorated

# --- API Endpoints ---

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    users = User.load_users()
    try:
        create_new_user(data['username'], data['name'], data['password'], users)
        return jsonify({'message': 'User created successfully!'})
    except ValueError as e:
        return jsonify({'message': str(e)}), 400

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    users = User.load_users()
    user_found = None
    for u in users:
        if u.username == data['username']:
            user_found = u
            break

    if user_found and verify_password(user_found.salt, user_found.hashed_password, data['password']):
        token = jwt.encode({
            'username': user_found.username,
            'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=1)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token})

    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/api/profile')
@token_required
def profile(current_user):
    return jsonify({'username': current_user.username, 'name': current_user.name})

# --- Frontend Routes ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/profile')
def profile_page():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run(debug=True)
