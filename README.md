# 🛒 E-commerce DAI
Repositorio del projecto web de la asignatura Desarrollo de Aplicaciones para Internet.

### Instalación local
> [!IMPORTANT]
> Ya que la aplicación se ejecuta en contenedores de Docker, es necesario tenerlo [instalado](https://docs.docker.com/engine/install/).

Para iniciar la aplicación clona el repositorio y ejecuta:
```bash
$ make up
```
Este comando levantará los contenedores correspondientes a la base de datos de mongoDB, otro para restaurar el backup de unos productos por defecto y por último el contenedor que contiene la aplicación.

Para acceder a la aplicación una vez los contenedores están levantados y en funcionamiento ve a tu navegador usando:
```
http://localhost:8000
```
