## Instalación
- Para ejecutar el proyecto con el chat se requiere linux
- Crear una carpeta para el proyecto
- Crear un entorno virtual dentro de la carpeta (python3 -m venv env)
- Clonar repositorio (A la misma altura del env)
- Activar el entorno virtual (source env/bin/activate)
- cd proyecto_cs
- pip install -r requirements.txt
- Crear una copia de .env_default con el nombre .env

## Base de datos
####Configuración
- En caso de no tener postgres ejecutar:

sudo apt-get install postgresql
- Ejecutar los siguientes comandos en la terminal: 

sudo su postgres -c psql  
CREATE USER work_user WITH PASSWORD 'work_pw';  
CREATE DATABASE workday_db OWNER work_user ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';  
GRANT ALL PRIVILEGES ON DATABASE workday_db TO work_user;  
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO work_user;  
ALTER USER work_user CREATEDB;  
ALTER ROLE work_user SUPERUSER;


## Redis
sudo apt install redis-server
###Comprobar instalacion redis
Ejecutar:
- redis-cli
- ping

Deberia obtener como resultado 'PONG'

## Superuser
Crear un superuser para acceder al admin con el comando
- python manage.py createsuperuser

##Ejecucion
Ejecute:
- python manage.py runserver
- Ingrese a 127.0.0.1:8000/admin
- Login con las credenciales del superuser
- Crear registros en el siguiente orden (Countries -> cities -> professions)
- Una vez se hayan creado al menos uno de cada uno ingrese a 127.0.0.1:8000/
- Proceda a registrarse y probar la aplicacion
