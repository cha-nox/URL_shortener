#!/bin/sh

# Attempting to create the database if it's not created yet
if [ ! -f "./.db_initialised" ]; then
    echo ">>> → Initialising database..."
    echo 'from db import create ; create()' | flask shell
    touch ./.db_initialised
    rm db.py
else
    echo ">>> ✓ Database is already initialised."
fi

# Running the app
python3 -m flask run --host=0.0.0.0