from ddtrace import tracer, patch_all
import os
import logging
import json
from flask import Flask, render_template, request
from datetime import datetime, timezone

# Configure Datadog settings programmatically
os.environ["DD_SERVICE"] = "py-playground"  # Replace with your service name
os.environ["DD_ENV"] = "test"              # Replace with your environment
os.environ["DD_LOGS_INJECTION"] = "true"   # Enable log correlation with traces

# Automatically instrument libraries (e.g., Flask, requests, etc.)
patch_all()


# Initialize Flask app
app = Flask(__name__)

# Custom JSON logging handler for file output


class JSONFileHandler(logging.FileHandler):
    def emit(self, record):
        log_entry = {
            'time': datetime.fromtimestamp(record.created, tz=timezone.utc).isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'name': record.name,
            'pathname': record.pathname,
            'lineno': record.lineno,
            'dd.env': record.__dict__.get("dd.env", os.environ.get("DD_ENV", "unknown")),
            'dd.service': record.__dict__.get("dd.service", os.environ.get("DD_SERVICE", "unknown")),
            'dd.version': record.__dict__.get("dd.version", os.environ.get("DD_VERSION", "unknown")),
            'dd.trace_id': record.__dict__.get("dd.trace_id", 0),
            'dd.span_id': record.__dict__.get("dd.span_id", 0),
        }
        with open(self.baseFilename, 'a') as file:
            file.write(json.dumps(log_entry) + '\n')


# Set up logging
log_file = "app.json.log"
json_handler = JSONFileHandler(log_file)

# Format for console output
console_format = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
                  '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
                  '- %(message)s')

# Apply logging configuration
logging.basicConfig(
    level=logging.INFO,
    format=console_format,
    handlers=[
        json_handler,              # Logs to a JSON file
        # logging.StreamHandler()    # Logs to the console
    ]
)
log = logging.getLogger(__name__)

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
