#!/bin/bash

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Executing tests"
python manage.py test

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
