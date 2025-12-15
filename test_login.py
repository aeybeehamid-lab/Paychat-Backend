import requests

BASE_URL = "http://127.0.0.1:5000"

# ---------------- TEST SIGNUP ----------------
print("---- Testing Signup ----")
signup_url = f"{BASE_URL}/signup"
signup_data = {
    "username": "testuser",
    "email": "test@example.com",
    "password": "12345"
}

try:
    response = requests.post(signup_url, json=signup_data)
    print("SIGNUP STATUS:", response.status_code)
    try:
        print("SIGNUP RESPONSE:", response.json())
    except Exception:
        print("SIGNUP RESPONSE RAW:", response.text)
except requests.exceptions.ConnectionError:
    print("ERROR: Could not connect to the server. Make sure app.py is running.")

# ---------------- TEST LOGIN ----------------
print("\n---- Testing Login ----")
login_url = f"{BASE_URL}/login"
login_data = {
    "email": "test@example.com",
    "password": "12345"
}

try:
    response = requests.post(login_url, json=login_data)
    print("LOGIN STATUS:", response.status_code)
    try:
        print("LOGIN RESPONSE:", response.json())
    except Exception:
        print("LOGIN RESPONSE RAW:", response.text)
except requests.exceptions.ConnectionError:
    print("ERROR: Could not connect to the server. Make sure app.py is running.")
