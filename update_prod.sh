#!/bin/bash
# timestamp def
timestamp() {
  date +"%Y-%m-%d_%H-%M-%S"
}

PRODUCTION="/opt/pythonchile_env/src/"
cd $PRODUCTION;

echo "- Pulling changes";
git remote -v;
git pull;


echo "- Installing requirements";
/opt/pythonchile_env/bin/pip install -r /opt/pythonchile_env/src/pythonchile_v2/requirements/pro.txt

echo "- Database migrations";
/opt/pythonchile_env/bin/python3.6 manage.py migrate --settings=pythonchile_v2.settings.production

echo "- Collect Static";
/opt/pythonchile_env/bin/python3.6 manage.py collectstatic --noinput --link --settings=pythonchile_v2.settings.production

echo "- Restart production";
/usr/bin/supervisorctl restart pythonchile_web
