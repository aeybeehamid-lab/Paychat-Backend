from flask import Flask, request, jsonify
from flask_cors import CORS
from models.user import create_user, get_user_by_email  # import user functions

app = Flask(__name__)
CORS(app)  # allow frontend requests

@app.route("/")
def home():
    return "PayChat backend is running 👍"

# ---------------- SIGNUP ROUTE ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()  # get JSON data from request
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    # Simple validation
    if not username or not email or not password:
        return jsonify({"error": "Please provide username, email, and password"}), 400

    # Check if user already exists
    if get_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    # Create user
    success = create_user(username, email, password)
    if success:
        return jsonify({"message": "User created successfully"}), 201
    else:
        return jsonify({"error": "Username or email already exists"}), 400

# ---------------- END ROUTE ----------------

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = get_user_by_email(email)
    if not user:
        return jsonify({"error": "User not found"}), 404

    if user["password"] != password:
        return jsonify({"error": "Incorrect password"}), 401

    return jsonify({"message": "Login successful"}), 200

