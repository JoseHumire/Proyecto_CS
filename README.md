## Instalación
- Clonar repositorio
- pip install -r requirements.txt
- Establecer env variables en .env (copiar de .env_default)

## Base de datos
####Configuración
- Ejecutar los siguientes comandos en la terminal:  
sudo su postgres -c psql  
CREATE USER username WITH PASSWORD 'password';  
CREATE DATABASE workday_db OWNER username ENCODING 'UTF8' LC_COLLATE = 'en_US.UTF-8' LC_CTYPE = 'en_US.UTF-8';  
GRANT ALL PRIVILEGES ON DATABASE workday_db TO username;  
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO username;  
ALTER USER username CREATEDB;  
ALTER ROLE username SUPERUSER;
