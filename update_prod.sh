#!/bin/bash

timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

PRODUCTION="/opt/pythonchile_env/src/"
PYENV="/opt/pythonchile_env/"

cd $PRODUCTION;

echo "- Pulling changes";
git remote -v;
git pull;


echo "- Installing requirements";
$PYENV/bin/pip install -r $PRODUCTION/pythonchile_v2/requirements/pro.txt

echo "- Database migrations";
$PYENV/bin/python3.6 manage.py migrate --settings=pythonchile_v2.settings.production

echo "- Collect Static";
$PYENV/bin/python3.6 manage.py collectstatic --noinput --link --settings=pythonchile_v2.settings.production

echo "- Restart production";
/usr/bin/supervisorctl restart pythonchile_web
