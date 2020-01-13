#!/bin/bash
set -e
NAME=pythonchile
TIMEOUT=90
BIND='127.0.0.1:9020'
USER='pythonchile'
DJANGO_SETTINGS_MODULE=pythonchile_v2.settings.production

. /opt/pythonchile_env/bin/activate
cd /opt/pythonchile_env/src

exec /opt/pythonchile_env/bin/gunicorn pythonchile_v2.wsgi --workers 3 --user=$USER --bind=$BIND