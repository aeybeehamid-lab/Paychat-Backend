from flask import Flask, request, jsonify
from flask_cors import CORS
from models.user import create_user, get_user_by_email

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "PayChat backend is running 👍"

# ---------------- SIGNUP ROUTE ----------------
@app.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Please provide username, email, and password"}), 400

    if get_user_by_email(email):
        return jsonify({"error": "Email already registered"}), 400

    if create_user(username, email, password):
        return jsonify({"message": "User created successfully"}), 201

    return jsonify({"error": "User creation failed"}), 400


# ---------------- LOGIN ROUTE ----------------
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


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)
GGg