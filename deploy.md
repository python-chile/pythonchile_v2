## Deploy en server
Requisitos:
- Ubuntu 18.04
- Python 3.6+
- virtualenv
- Nginx
- Postgres
- Supervisor


#### Crear entorno virutal
```
cd /opt/
virtualenv pythonchile_env -p python3
```

#### Clonar repositorio
```
git clone https://github.com/python-chile/pythonchile_v2.git src
```

#### Instalar reqs
```
pip install -r requirements/pro.txt
```

#### Setear variables de entorno
Crear el archivo postactivate del entorno virtual y setear las variables necesarias.
```
#!/bin/bash
# This will be run after this virtualenv is activated.

export SECRET_KEY="__replace_me_with_super_secret_key__"
export DB_NAME="pythonchile_web"
export DB_USER="postgres"
export DB_PASS="__replace_me_with_super_secret_key__"
export DB_SERVICE="localhost"
```
Luego agregar la llamada a ```postactivate``` desde el archivo ```activate``` del entorno virtual. En la última linea del archivo ```activate``` agregar:
```
source ./postactivate
```

#### Configuración DB
Entrar a psql con el usuario postgres.
```
sudo -u postgres psql
```
Crear base de datos.
```
CREATE DATABASE pythonchile_web;
```

Crear usuario para la base de datos (cambiar la contraseña!).
```
CREATE USER pythonchile_user WITH PASSWORD 'replaceme-with-password';
```

Configuraciones generales recomendadas para [Django](https://docs.djangoproject.com/en/2.2/ref/databases/#optimizing-postgresql-s-configuration).
```
ALTER ROLE pythonchile_user SET client_encoding TO 'utf8';
ALTER ROLE pythonchile_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE pythonchile_user SET timezone TO 'UTC';
```

Entregar todos los privilegios al usuario para la DB.
```
GRANT ALL PRIVILEGES ON DATABASE pythonchile_web TO pythonchile_user;
```
Para salir de psql.
```
\q
```

### Instalar Supervisor
### Instalar Gunicorn