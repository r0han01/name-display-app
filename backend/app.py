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

# Serve the HTML page at the root URL with styled content
@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to the Flask App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f9;
                color: #333;
            }
            .header {
                background-color: #007bff;
                color: white;
                padding: 15px 0;
                text-align: center;
            }
            .container {
                max-width: 800px;
                margin: 40px auto;
                padding: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                text-align: center;
            }
            h1 {
                font-size: 2.5rem;
                color: #007bff;
            }
            p {
                font-size: 1.2rem;
                margin-top: 10px;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                color: white;
                background: #007bff;
                padding: 10px 15px;
                border-radius: 5px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
            a:hover {
                background: #0056b3;
            }
            .name-list {
                margin-top: 30px;
                text-align: left;
            }
            .name-list ul {
                list-style: none;
                padding: 0;
            }
            .name-list li {
                padding: 8px;
                background-color: #e9ecef;
                margin: 5px 0;
                border-radius: 4px;
            }
        </style>
    </head>
    <body>
        <div class="header">
            <h1>Welcome to the Flask Application</h1>
        </div>
        <div class="container">
            <h2>Hi! Backend here!</h2>
            <p>This is a simple Flask application with dynamic routing and a styled home page.</p>
            <a href="/api/names">See the List of Names</a>

            <div class="name-list">
                <h3>Names List:</h3>
                <ul>
                    <li>Alice</li>
                    <li>Bob</li>
                    <li>Charlie</li>
                    <li>Diana</li>
                    <li>Eve</li>
                </ul>
            </div>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Backend runs on port 5000

