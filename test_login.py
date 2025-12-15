import requests

url = "http://127.0.0.1:5000/login"
data = {
    "email": "test@example.com",
    "password": "12345"
}

response = requests.post(url, json=data)

print("STATUS:", response.status_code)
print("RAW:", response.text)
