- A web application on Python.
- A simple web-based application for Human resource management. 
- The application with only two entities: “Department” and “Employee”, related as one to many.

**TO DO**
**APPOINTMENT OF ENVIRONMENTAL VARIABLES** 
- Open your .bashrc file on your local machine;
- Define there next environmental variables in separate lines like key="value" pairs:  
  - `export SECRET_KEY="the_value_of_your_secret_key"`
  - `export GROW_DB_NAME="the_name_of_your_database"`
  - `export DB_USER="the_name_of_database's_owner"`
  - `export DB_PASSWORD="the_database's_password"`
- Open your settings.py file;
- Replace in it:
  - line containing SECRET_KEY with line `SECRET_KEY = os.environ.get('SECRET_KEY')`
  - replace DATABASE settings with the following:
  ```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('GROW_DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': '*',
        'PORT': '5432',
    },
    'OPTIONS': {
        'isolation_level': psycopg2.extensions.ISOLATION_LEVEL_SERIALIZABLE,
    },
}```
- Also define some GITHUB REPO SECRETS for CI/CD correct work, specifically SECRET_KEY, GROW_DB_NAME, DB_USER, 
DB_PASSWORD with the same values as in .bashrc file.

[![Pylint Actions Status](https://github.com/Pasha-Ignatyuk/grow/workflows/Pylint/badge.svg)] 
(https://github.com/Pasha-Ignatyuk/grow/actions)

[![Coverage Status](https://coveralls.io/repos/github/Pasha-Ignatyuk/grow/badge.svg?branch=master)]
(https://coveralls.io/github/Pasha-Ignatyuk/grow?branch=master)
