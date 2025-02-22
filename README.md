(WIP) This app provides a simple interface and will generates various events and traces, making it an ideal tool for exploring Datadog's functionality and validating its integration with real-world applications.
Follow the steps below after cloning this repo.

#### Environment:
- macOS
- Python@3.11
- Pip3
- Virtual Environment
- Flask
- HTML
- Datadog Agent
- Datadog APM

## Web Application
1. Create a virtual environment. The virtual environment is a one-time setup that stores the installed dependencies for your project
```
python3.11 -m venv myvenv
```

2. Activate the environment
```
source myvenv/bin/activate
```

3. Install the dependencies
```
pip3 install -r requirements.txt
```

#### The file structure should look like this
```
datadog-apm-demo/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
├── myvenv/
└── templates/
    └── index.html
```

4. Run the Application 
```
python3 app.py
```
This Flask app will serve a webpage when you access http://127.0.0.1:5000/ in your browser.

# Datadog
## Logs
This app logs messages in JSON format to a file named `app.json.log`. Each log entry includes details such as timestamp, log level, message, logger name, file path, and line number.

1. Install the Python Integration.
   
2. Update the `datadog.yaml` configuration file:
```
logs_enabled: true
```

3. Configure the Datadog Agent to monitor the app.json.log file:
- Create a `python.d/` folder in the `conf.d/` Agent configuration directory.
- Create a file `conf.yaml` in the `conf.d/python.d/` directory with the following content and update the path of your log file:
```
init_config:

instances:

##Log section
logs:

  - type: file
    path: "/Users/user/datadog-apm-demo/app.json.log" 
    service: "flask-app"
    source: python
    sourcecategory: sourcecode
```
4. Restart the Agent

Log File Output: The JSONFileHandler ensures logs are saved in JSON format to the app.json.log file.

[Log Collection And Integrations](https://docs.datadoghq.com/logs/log_collection/?tab=host)

## APM
Host Based - Datadog Agent on the same host as application.

The Datadog Agent is used to send traces from our tracing libraries. Make sure you're in the virtual environment when you install the Datadog Python package or any other dependecy.

1. Install Datadog APM tracing library for Python (ddtrace)
```
pip3 install ddtrace
```

We configured Datadog APM programmatically in this Flask app. If you decide to automatically instrument this app use `ddtrace-run` instead, you would run your app like this:
```
DD_SERVICE="py-playground" DD_ENV="test" DD_LOGS_INJECTION=true ddtrace-run python app.py
```

2. Run the Application 
```
python3 app.py
```

## Correlating Python Logs and Traces

* Add global tags in the `datadog.yaml` file which would define metadata that will automatically be attached to all logs, metrics, and traces sent from your application or infrastructure to Datadog. These tags help you filter, group, and analyze your data more effectively within the Datadog platform. Add tags in the format `key:value`, separated by commas.
  
* This script is supposed to include the Datadog-specific attributes (`dd.env`, `dd.service`, `dd.version`, `dd.trace_id`, and `dd.span_id`) in the log entries. These attributes will appear in the JSON log records, enabling correlation between logs and traces in Datadog.

Log Injection for File Logs: Attributes like `dd.trace_id`, `dd.span_id`, `dd.env`, and `dd.service` are extracted from the log record's context and included in the JSON logs.

#### Once you're done working with the app, deactivate the virtual environment:
```
deactivate
```

[Agent Commands](https://docs.datadoghq.com/agent/configuration/agent-commands/)