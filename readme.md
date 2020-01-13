Pythonchile.cl web
=======

Este es código del [sitio de Python Chile](http://pythonchile.cl) desarrollado usando [Django](https://www.djangoproject.com/) y [Wagtail](https://wagtail.io/).

### Levantar usando Docker
Debes tener instalado docker en tu sistema.
```
docker build -t pythonchile .
docker run -p 8000:8000 pythonchile
```

### Levantar usando virtualenv
#### Instalar virtualenv
```
sudo apt-get install python-virtualenv
```

#### Crear entorno
```
virtualenv pythonchile_env -p python3
```

#### Entrar al entorno virtual y activarlo
```
cd pythonchile_env/
source bin/activate
```

### Usuarios de desarrollo
##### Rol: username / pass

- Admin: admin / local_password
- Editor: editor / local_password
- Moderador: moderador / local_password


## Por hacer
- [x] Blog
- [x] Registro de usuario
- [x] Integrar HTML básico
- [x] Licencia
- [x] Registro de usuario
- [x] Licencia
- [ ] Deploy