# Python Chile Website

Repositorio que contiene el código con el cual se construye el
[sitio de Python Chile](http://pythonchile.cl).

La versión actual está desarrollada usando
[Django](https://www.djangoproject.com/) y [Wagtail](https://wagtail.io/).

## Configuración Local

Para comenzar el servidor localmente y probar alguna funcionalidad
nueva que quieras contribuir, puedes usar Docker o un simple entorno
virtual.

### Usando Docker

Debes tener instalado docker en tu sistema, y luego solo ejecutar:

```
docker build -t pythonchile .
docker run -p 8000:8000 pythonchile
```

### Usando entornos virtuales

* Installar `virtualenv` o `venv` (Ubuntu)
    Recuerda que solo debes escoger uno:
    ```
    # virtualenv
    sudo apt-get install python-virtualenv
    # venv
    sudo apt-get install python-venv
    ```

    Algunas distribuciones Linux tendrán `venv` ya instalado con Python
    en el sistema, con lo que puedes omitir este paso.

* Crear entorno:
    ```
    # virtualenv
    virtualenv pythonchile_env -p python3
    # venv
    python3 -m venv pythonchile_env
    ```

    Algunos sistemas tendrán un ejecutable llamado `python` (sin el 3)
    por defecto, puedes probar que sea la versión 3 ejecutando: `python --version`
    en una terminal.

* Activación del entorno virtual
    ```
    source pythonchile_env/bin/activate
    ```

* Instalar los requerimientos:
    ```
    pip install -r requirements/dev.txt
    ```

### Usuarios de desarrollo

* Rol: username / pass
 - Admin: admin / local_password
 - Editor: editor / local_password
 - Moderador: moderador / local_password
