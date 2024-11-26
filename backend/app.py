from flask import Flask, jsonify, render_template
from flask_cors import CORS  # Import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# A simple list of names
names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

# Serve the names API
@app.route('/api/names', methods=['GET'])
def get_names():
    return jsonify(names)

# Serve the HTML page at the root URL
@app.route('/')
def home():
    return render_template('index.html')  # This will look for 'index.html' in the 'templates' folder

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Backend runs on port 5000
