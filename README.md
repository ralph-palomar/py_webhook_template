# py_webhook_template
A microservice written in Python Flask framework and other utilities, which serves as a template when starting a new application. It provides all the boilerplate codes, and you just need to provide the application logic and/or other helper functions. Most common use case is for setting up a webhook.

**Current Features**
1. CORS Validation - performs preflight check and lets you control values that are allowed in these HTTP headers:
    * Access-Control-Allow-Origin
    * Access-Control-Allow-Headers
    * Access-Control-Allow-Methods
    

2. Supports configurable rotating file loggers up to a max file size and count.

3. Gives you the flexibility to add more API routes as necessary, or expose functions as API routes, which is a desirable feature of Flask.

4. Externalizes environment settings through the `run.sh` bash script.
5. Only runs on Linux which natively supports Python 3.x. Ensure that you're using the latest version of `python`.
6. Authentication is not supported as this is designed for webhooks. For added security for cases other than webhooks, make sure to implement your own authentication policy.

**What you need to know**
1. Set the `base_path` variable in main.py to your desired value. This must be unique for every instance of the application.
2. Specify an available internal port for every instance of the application in the run.sh file: `waitress-serve --port=8080 main:api`
3. Make sure that `requirements.txt` is always updated with project dependencies, and their desired versions.
4. If you're using a reverse proxy such as `nginx`, make sure to add the base path in the `sites-available` config file.