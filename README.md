# 🛒 E-commerce DAI
Repositorio del projecto web de la asignatura Desarrollo de Aplicaciones para Internet.

## Características de la API
- Obtener todos los productos
- Obtener un producto
- Crear productos nuevos
- Actualizar un produto
- Eliminar un producto
- Puntuar un producto con una nota desde 1 estrella hasta 5 estrellas

## Instalación local
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
## Imágenes - Vista previa

### Homepage

![ecommerce](https://github.com/user-attachments/assets/3339196a-8d84-4c15-8efc-1cf7517caf50)

### Vista de categoría

![men](https://github.com/user-attachments/assets/cc4c42a6-4a1e-4ebf-9022-3dfa6257b5f3)

### API

![api](https://github.com/user-attachments/assets/bf9f55ea-30a8-4ddb-921e-5c65a3ca6550)
