#!/bin/bash
GUNI_CONFIG="/opt/src/gunicorn.conf.py"

exec gunicorn --config "$GUNI_CONFIG" \
              wsgi:app -w 1
