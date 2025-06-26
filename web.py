from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define route and view function
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)