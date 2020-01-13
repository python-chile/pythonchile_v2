#!/bin/bash
set -e
LOGFILE=/opt/pythonchile_env/logs/gunicorn.log
LOGDIR=/opt/pythonchile_env/logs/
NAME=pythonchile
TIMEOUT=90
BIND='127.0.0.1:9020'
USER='pythonchile'
DJANGO_SETTINGS_MODULE=pythonchile_v2.settings_production
. /opt/pythonchile_env/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE

exec /opt/pythonchile_env/bin/gunicorn \
--workers 3 \
--user=$USER \
--bind=$BIND \
--log-level=$LOG_LEVEL \
--log-file=$LOGFILE \
pythonchile_v2.wsgi