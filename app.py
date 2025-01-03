from ddtrace import tracer, patch_all
import os

# Configure Datadog settings programmatically
os.environ["DD_SERVICE"] = "py-playground"  # Replace with your service name
os.environ["DD_ENV"] = "test"              # Replace with your environment
os.environ["DD_LOGS_INJECTION"] = "true"   # Enable log correlation

# Automatically instrument libraries (e.g., Flask, requests, etc.)
patch_all()

from flask import Flask, render_template

# Initialize Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Run the app on localhost
if __name__ == '__main__':
    app.run(debug=True)
