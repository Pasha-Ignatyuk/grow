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

- Also define some GITHUB REPO SECRETS for CI/CD correct work, specifically SECRET_KEY, GROW_DB_NAME, DB_USER, 
DB_PASSWORD with the same values as in .bashrc file.

**To install dependencies and run project You must:**  
- Copy the project folder to your local computer;
- Execute the following commands in the terminal: 
  - python -m venv venv
  - source venv/bin/activate
  - pip install -r requirements.txt
  - python manage.py migrate
  - python manage.py createsuperuser
  - enter name of superuser, e-mail, password and password confirmation
  - python manage.py runserver

To run pylint check manually execute the following command in the terminal:  
- pylint --load-plugins pylint_django hrm/department

[![Pylint Actions Status](https://github.com/Pasha-Ignatyuk/grow/workflows/Pylint/badge.svg)](https://github.com/Pasha-Ignatyuk/grow/actions)

[![Coverage Status](https://coveralls.io/repos/github/Pasha-Ignatyuk/grow/badge.svg?branch=master)](https://coveralls.io/github/Pasha-Ignatyuk/grow?branch=master)
