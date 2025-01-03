(WIP) This app provides a simple interface and will generates various events and traces, making it an ideal tool for exploring Datadog's functionality and validating its integration with real-world applications.
Follow the steps below after cloning this repo.

#### Environment:
- macOS
- Python@3.11
- Pip
- Virtual Environment
- Flask
- HTML
- Datadog Agent
- Datadog APM

## Web Application
1. Create a virtual environment
The virtual environment is a one-time setup that stores the installed dependencies for your project.
```python3.11 -m venv myvenv```

2. Activate the environment
```source myvenv/bin/activate```

3. Install the dependencies
```pip install -r requirements.txt```

#### The file structure should look like this
```
datadog-apm-demo/
│
├── app.py
├── README.md
├── requirements.txt
├── myvenv/
└── templates/
    └── index.html
```

4. Run the Application 
```python3 app.py```
This Flask app will serve a webpage when you access http://127.0.0.1:5000/ in your browser.

## Datadog APM
Host Based - Datadog Agent on the same host as application.
The Datadog Agent is used to send traces from our tracing libraries.
Make sure you're in the virtual environment when you install the Datadog Python package or any other dependecy.

1. Install Datadog APM tracing library for Python (ddtrace)
```pip install ddtrace```

We configured Datadog APM programmatically in this Flask app.
If you decide to automatically instrument this app use `ddtrace-run` instead, you would run your app like this:
```DD_SERVICE="py-playground" DD_ENV="test" DD_LOGS_INJECTION=true ddtrace-run python app.py```

2. Run the Application 
```
python3 app.py
```

3. Once you're done working with the app, deactivate the virtual environment
```
deactivate
```

[Agent Commands](https://docs.datadoghq.com/agent/configuration/agent-commands/)