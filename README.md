[![YourActionName Actions Status](https://github.com/chiahsoon/flask-scaffold/workflows/flask-scaffold/badge.svg)](https://github.com/chiahsoon/flask-scaffold/actions)

## Overview
The goal of this repository is to provide an easy-to-setup Flask backend API server for rapid prototyping/POC projects.
This file layout is basically copied from traditional Java's file organisation, purely because of personal preferences.
It has a few basic features, namely:

1. Configuration Management.
2. Session-based Authentication. (using Cookies)
3. ORM capability using _[flask-sqlalchemy](https://github.com/pallets/flask-sqlalchemy)_.
4. Production ready HTTP server with Gunicorn.
5. Docker Compose for quick & easy deployment to container environments.

### Project Layout
* `wsgi.py` is the entry point of the Flask application, that Gunicorn binds to.
* `/controllers` will contain all the api/controller routes that the front end requires.
* `/models` will contain the data access object definitions.
* `/services` will contain the business logic.
* `/views` will contain the wrappers for incoming request bodies or outgoing response bodies.
* `/utilities` contains everything in between; constants, database initialisations, etc.
* `/configurations` handles the external environmental configurations.
  
### Configuration Management
* Configuration can be managed through _/configuration/*.yaml_ files or through environment variables.
  * The keys in the environment variables should be the uppercased versions of their _.yaml_ counterparts.
    * For example, if `db_name` is defined in your _.yaml_ file, then the corresponding environment variable should be `DB_NAME`.
  * The naming convention for the configuration files is: _{environment name}.yaml_ .
* You are encouraged to define configurations in the _.yaml_ files, because:
  * They are used as the base values which will only be overridden if the corresponding environment variables are present.
  * Nested environmental variables are currently **not yet supported**.
* Although default files _dev.yaml_ and _docker-dev.yaml_ are provided, **PLEASE REMEMBER TO NOT COMMIT PRODUCTION CONFIGURATIONS TO YOUR REMOTE REPOSITORIES**.


## Manual Setup

These instructions were tested to work on a Mac, but should work for most common unix based systems as well. 
Unless otherwise stated, these commands should be run in the **root** of this repository.

1. Set up a Python virtual environment, activate and install the necessary packages.

    ```
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
    ```
    1. If you install other packages in the future, you can add them to the requirements.txt file.
        ```
        pip3 freeze > requirements.txt
        ``` 
2. Set up your database. You can easily configure the database settings via the _/configurations_ folder.
   If you are using MySQL, you can replicate these steps:
   
      1. Download mysql 8.0.x using [Homebrew](https://brew.sh/), then start the MySQL server.
          ```
         brew install mysql@8.0
         brew services start mysql
         ```
      2. Create a database/schema for your data.
          ```
          mysql -u root < "create schema scaffold;"
          ```

3. Check and change the values in _/configurations_ accordingly.
4. Export environment variables as necessary.
    ```
    export ENV=dev # Defaults to 'dev'
    export PORT=8080 # Defaults to '8080'
   ```
5. Start the Flask development server, or the Gunicorn WSGI server.
    ```
    flask run --host=127.0.0.1 --port=8080 # dev server
    # OR
    gunicorn --bind 127.0.0.1:8080 wsgi:app # Gunicorn WSGI server
    ```

## Docker-Compose Setup
1. Install Docker through _brew_ if you haven't already. Alternatively, you can also install 
   [Docker Desktop](https://www.docker.com/products/docker-desktop) if you want to use its GUI. 
   ```
   brew install docker
   ```
2. Build the Dockerfile located at the root of this directory within Docker-Compose.
   ```
   docker-compose build
   ```
3. Start Docker-Compose.
   ```
   docker-compose up
   ```
4. Stop Docker-Compose.
    ```
    docker-compose down
    ```


## Useful Resources
* [Blueprints](https://www.youtube.com/watch?v=WteIH6J9v64)
* [Connecting to MySQL](https://www.youtube.com/watch?v=Tu4vRU4lt6k)
* [Python MySQL Driver Error](https://stackoverflow.com/questions/22252397/importerror-no-module-named-mysqldb)
* [One To Many](https://www.youtube.com/watch?v=juPQ04_twtA), [One To One](https://www.youtube.com/watch?v=JI76IvF9Lwg) 
and [Many To Many](https://www.youtube.com/watch?v=OvhoYbjtiKc) relationships.