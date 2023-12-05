#!/bin/bash

echo "Running migrations..."

# Run the Django migrations
python3 /usr/src/app/manage.py migrate core

echo "Starting gunicorn..."

# Start gunicorn
gunicorn number_cruncher.wsgi:application --bind=0.0.0.0:8000 --workers=4 --chdir=/usr/src/app
