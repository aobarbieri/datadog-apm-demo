from ddtrace import tracer, patch_all
import os

# Configure Datadog settings programmatically
os.environ["DD_SERVICE"] = "py-playground"  # Replace with your service name
os.environ["DD_ENV"] = "test"              # Replace with your environment
os.environ["DD_LOGS_INJECTION"] = "true"   # Enable log correlation

# Automatically instrument libraries (e.g., Flask, requests, etc.)
patch_all()

from flask import Flask, render_template, request
import logging
import json

# Initialize Flask app
app = Flask(__name__)

# Custom JSON logging handler
class JSONFileHandler(logging.FileHandler):
    def emit(self, record):
        log_entry = {
            'time': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'pathname': record.pathname,
            'lineno': record.lineno
        }
        with open(self.baseFilename, 'a') as file:
            file.write(json.dumps(log_entry) + '\n')

# Set up logging with JSON format
log_file = "app.json.log"
json_handler = JSONFileHandler(log_file)
json_handler.setFormatter(logging.Formatter('%(asctime)s'))

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        json_handler,              # Logs to a JSON file
        logging.StreamHandler()          # Logs to the console
    ]
)

# Define a route for the homepage
@app.route('/')
def home():
    logging.info("App is running and the home page is loaded.")
    return render_template('index.html')

@app.route('/button_click', methods=['POST'])
def button_click():
    logging.info("Button was clicked.")
    return "Button click logged!"

# Run the app on localhost
if __name__ == '__main__':
    logging.info("Starting the Flask app...")
    app.run(debug=True)
