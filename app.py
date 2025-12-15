from flask import Flask, request, jsonify
from flask_cors import CORS
from models.user import create_user, get_user_by_email, verify_password
from auth import token_required
import jwt
from datetime import datetime, timedelta
app = Flask(__name__)
CORS(app)

SECRET_KEY = "paychat_secret_key"  # change later for production

@app.route("/")
def home():
    return "PayChat backend is running 👍"

# ---------------- SIGNUP ----------------
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

# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = get_user_by_email(email)

    if not user:
        return jsonify({"error": "User not found"}), 404

    if not verify_password(password, user["password"]):
        return jsonify({"error": "Incorrect password"}), 401

    token = jwt.encode(
        {
            "user_id": user["id"],
            "email": user["email"],
            "exp": datetime.utcnow() + timedelta(hours=24)
        },
        SECRET_KEY,
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful",
        "token": token
    }), 200


# ---------------- RUN SERVER ----------------
if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)
@app.route("/profile", methods=["GET"])
@token_required
def profile():
    user = request.user
    return jsonify({
        "message": "Profile accessed",
        "user": user
    }), 200

if __name__ == "__main__":
    app.run(debug=True)

print(app.url_map)

