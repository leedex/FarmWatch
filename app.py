from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to FarmWatch!"

if __name__ == '__main__':
    # Run the Flask app with debug mode enabled and port set to 5001
    app.run(debug=True, port=5001)
