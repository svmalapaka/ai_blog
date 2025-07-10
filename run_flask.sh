#!/bin/bash

source venv/bin/activate
export FLASK_APP=ai_quote_app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=8080
