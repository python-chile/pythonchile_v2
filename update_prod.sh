#!/bin/bash

timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

PRODUCTION="/opt/pythonchile_env/src"
PYENV="/opt/pythonchile_env"

cd $PRODUCTION;
echo "$(timestamp)" >> deploys_log.txt

echo "- Pulling changes"
git remote -v
git pull
git log -1 >> deploys_log.txt

echo "- Installing requirements";
$PYENV/bin/pip install -r $PRODUCTION/requirements/pro.txt || echo "Error installing requirements" >> deploys_log.txt

echo "- Database pre-migrations backup"
pg_dump pythonchile_web > ~/backups/pythonchile_web_.$(timestamp).sql || echo "Error creating DB backup" >> deploys_log.txt

echo "- Database migrations";
$PYENV/bin/python manage.py migrate --settings=pythonchile_v2.settings.production || echo "Error db migrations" >> deploys_log.txt

echo "- Collect Static";
$PYENV/bin/python manage.py collectstatic --noinput --link --settings=pythonchile_v2.settings.production || echo "Error collect static" >> deploys_log.txt

echo "- Restart production";
/usr/bin/supervisorctl restart pythonchile_web || echo "Error restart supervisorctl" >> deploys_log.txt
