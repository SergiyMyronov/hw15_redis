Homework 15
Django redis cache demonstration

Overview

This web application demonstrates Django redis cache.

The main features that have currently been implemented are:

    There are models for cities, suppliers, products and customers.
    Users can view list and detail information for models products, suppliers and customers.
    Users cen view customers with related products.
    Pages: 
        http://127.0.0.1:8000/redis_cache/cust/
        http://127.0.0.1:8000/redis_cache/prod/
    are cached for 20 seconds.

    Admin users can manage models. 

Quick Start

To get this project up and running locally on your computer:

    Set up the Python development environment. We recommend using a Python virtual environment.
    Assuming you have Python setup, run the following commands (if you're on Windows you may use py or py -3 instead of python to start Python):

    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py runserver

    To generate new data run the management command:
    python3 manage.py makedata

    There is a dump of some data in the file redis_cache/fixtures/db.json
    Available users: 
    "admin" with password "adm123456" - superuser

    Open a browser to http://127.0.0.1:8000/admin/ to open the admin site.

    Open tab to http://127.0.0.1:8000/redis_cache/cust/ to see all customers with related products.
