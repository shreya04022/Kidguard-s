from flask import Flask, request, jsonify, session
from flask_cors import CORS

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Replace with a more secure key
CORS(app)

# Mock databases
users = {}  # Format: {"email": {"name": "Parent Name", "password": "password"}}
activities = {  # Example child activity data
    "child1": [
        {"time": "10:00 AM", "app": "YouTube", "duration": 30},
        {"time": "11:30 AM", "app": "WhatsApp", "duration": 20},
        {"time": "01:00 PM", "app": "Instagram", "duration": 40},
    ]
}


# User Sign-Up API
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.json
    email = data.get("email")
    name = data.get("name")
    password = data.get("password")

    if email in users:
        return jsonify({"error": "Email already exists"}), 400

    # Save user data
    users[email] = {"name": name, "password": password}
    return jsonify({"message": "Sign-up successful"}), 200


# User Login API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    # Check if email and password match
    if email not in users or users[email]["password"] != password:
        return jsonify({"error": "Invalid email or password"}), 401

    # Store user in session
    session['email'] = email
    return jsonify({"message": "Login successful", "name": users[email]["name"]}), 200


# Fetch Child Activity API
@app.route('/api/activity/<child_id>', methods=['GET'])
def get_activity(child_id):
    if child_id not in activities:
        return jsonify({"error": "Child not found or no activity data"}), 404

    return jsonify({"activity": activities[child_id]}), 200


# Logout API
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('email', None)
    return jsonify({"message": "Logged out successfully"}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)