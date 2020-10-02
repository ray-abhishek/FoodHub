
## Food Hub
 A Django Application to perform CRUD Operations on Entities such as Merchant, Item, Store, Order.

<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangoproject120x25.gif" border="0" alt="A Django project." title="A Django project." /></a>
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/)

## Motivation
Idea is to gain a understanding of how Django and relevant frameworks such as Django Rest Framework, pytest etc work with an emphasis on producing scalable and maintainable code.

## Frameworks used

- Django 3.1
- MySql 5.7
- Django Rest Framework 3.12
- pytest-django 3.10.0

## Features
- Ability to add/view(list, detail)/update/delete entries for Merchant, Item, Store and Orders.
- Ability to see list of stores/items/orders belonging to a Merchant.
- Ability to see list of Orders placed for a particular store. 


## Getting the Application up and running. 
- git clone https://github.com/ray-abhishek/FoodHub.git
- virtualenv env -> To create virtualenv
- source env/bin/activate -> To activate virtual environment in which all the project dependencies will be installed.
- Navigate to Directory containing requirements.txt 
- pip3 install -r requirements.txt -> Install project dependencies
- python3 manage.py migrate  -> To apply migrations in Local Database. 
- python3 manage.py runserver -> To start server


## Testing - Setup and Execution 
- Navigating to Directory containing test_requirements.txt.
- pip3 install -r test_requirements.txt -> Install Dependencies for Testing
- Run command: pytest -> to execute the tests. 


## API Reference
- To be updated. 
