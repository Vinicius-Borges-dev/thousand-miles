from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS()

@app.route('/')
def index():
    return jsonify({'message': 'Hello, World!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')