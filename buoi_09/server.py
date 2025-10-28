from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

# Load JSON data from files
def load_book_data():
    file_path = os.path.join(os.path.dirname(__file__), 'bai1_khoahoc.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_user_data():
    file_path = os.path.join(os.path.dirname(__file__), 'bai2_users.json')
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

@app.route('/')
def home():
    return "Xin chào từ Flask trên mọi địa chỉ IP!"

@app.route('/api/book', methods=['GET'])
def get_book():
    try:
        book_data = load_book_data()
        return jsonify(book_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/user/<username>', methods=['GET'])
def get_user(username):
    try:
        users_data = load_user_data()
        for user in users_data['users']:
            if user['username'] == username:
                return jsonify(user)
        return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/subtract', methods=['POST'])
def subtract():
    try:
        data = request.get_json()
        if not isinstance(data, dict) or 'a' not in data or 'b' not in data:
            return jsonify({"error": "Invalid input. Requires 'a' and 'b' numbers"}), 400
        
        result = data['a'] - data['b']
        return jsonify({
            "a": data['a'],
            "b": data['b'],
            "result": result
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)