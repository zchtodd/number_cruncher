#!/bin/sh
watchmedo auto-restart --directory=./ --pattern=*.py --recursive -- celery -A number_cruncher worker "$@" --loglevel=info
