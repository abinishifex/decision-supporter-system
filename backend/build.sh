#!/usr/bin/env bash
# exit on error
set -o errexit

# Only CD into backend if we're not already in it
if [ -d "backend" ]; then
    cd backend
fi

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
