# biblioteca_fastapi

## 👨‍💻 Desarrollo Realizado Por  

**Ing. Juan Sebastián Gómez Díaz**  
*Ingeniero de Sistemas y Computación*  
📍 *Universidad Tecnológica de Pereira*  


# Biblioteca API - Guía de Instalación y Ejecución

Este proyecto es una API desarrollada con FastAPI, PostgreSQL y Docker para gestionar una biblioteca. Sigue estos pasos para instalar y ejecutar la aplicación correctamente.

## 1. Requisitos Previos
Antes de comenzar, asegúrate de tener instalados los siguientes programas:

- [Git](https://git-scm.com/)
- [Docker y Docker Compose](https://www.docker.com/get-started)

## 2. Clonar el Repositorio
Clona el repositorio desde GitHub usando el siguiente comando:

```sh
  git clone https://github.com/SebaxtriUTP/biblioteca_fastapi.git
```

Luego, entra en la carpeta del proyecto:

```sh
  cd biblioteca-fastapi
```

## 3. Configurar Variables de Entorno
Crea un archivo `.env` en la raíz del proyecto y agrega las siguientes variables de entorno:

```env
DATABASE_URL=postgresql://postgres:postgres@db/biblioteca_fastapi
SECRET_KEY=tu_clave_secreta
```

## 4. Construir y Levantar los Contenedores con Docker
Ejecuta el siguiente comando para levantar la base de datos y la aplicación:

```sh
  docker-compose up --build -d
```

Este comando hará lo siguiente:
- Construir las imágenes de Docker si no existen.
- Levantar los contenedores de la aplicación y la base de datos en segundo plano (`-d`).

## 5. Verificar que los Contenedores Están Corriendo
Para asegurarte de que los contenedores están activos, usa:

```sh
  docker ps
```

Deberías ver los contenedores `app` (FastAPI) y `db` (PostgreSQL) ejecutándose.

## 6. Aplicar Migraciones a la Base de Datos
Ejecuta las migraciones necesarias:

```sh
  docker exec -it nombre_del_contenedor_app alembic upgrade head
```

## 7. Acceder a la Aplicación
Si todo ha funcionado correctamente, la aplicación estará disponible en:

🔗 **FastAPI Docs:** [http://localhost:8000/docs](http://localhost:8000/docs)

🔗 **API en JSON:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 8. Apagar y Eliminar los Contenedores
Cuando termines de usar la aplicación, puedes apagar los contenedores con:

```sh
  docker-compose down
```

Si deseas eliminar también los volúmenes de datos, usa:

```sh
  docker-compose down -v
```

## 9. Solución de Problemas

### Error de permisos en PostgreSQL
Si ves un error de permisos al ejecutar la base de datos, intenta acceder al contenedor de PostgreSQL y otorgar permisos manualmente:

```sh
  docker exec -it nombre_del_contenedor_db psql -U postgres
  GRANT ALL PRIVILEGES ON DATABASE biblioteca_fastapi TO myuser;
```

### El contenedor no se inicia correctamente
Si los contenedores no se inician, revisa los logs:

```sh
  docker-compose logs -f
```

## Acceder a la Documentación de la API con Swagger

FastAPI genera automáticamente documentación interactiva utilizando Swagger UI. Para acceder a ella, sigue estos pasos:

### 1. Levantar el Servidor
Si la aplicación no está en ejecución, inicia el servidor con el siguiente comando:

```bash
uvicorn main:app --reload
```

### 2. Acceder a Swagger UI
Una vez que el servidor esté en funcionamiento, abre tu navegador y dirígete a:

```
http://127.0.0.1:8000/docs
```

### 3. Explorar los Endpoints
Desde la interfaz de Swagger UI, podrás:
- Ver todos los endpoints disponibles.
- Probar los endpoints directamente desde el navegador.
- Ver los modelos de solicitud y respuesta.

### 4. Alternativa: ReDoc
FastAPI también proporciona documentación con **ReDoc**. Para acceder a ella, usa:

```
http://127.0.0.1:8000/redoc
```

### Preguntas Adicionales

#### ¿Cómo manejarías la autenticación y autorización en la API?
- Usaría **OAuth2 con JWT** para la autenticación.
- Implementaría **FastAPI OAuth2PasswordBearer** para gestionar tokens.
- Asignaría **roles y permisos** con un sistema de control de acceso basado en RBAC o ABAC.

#### ¿Qué estrategias utilizarías para escalar la aplicación?
- **Escalado horizontal:** Implementar contenedores con **Docker y Kubernetes**.
- **Balanceo de carga:** Usar **NGINX o un servicio en la nube**.
- **Caching:** Implementar **Redis** para reducir la carga en la base de datos.
- **Optimización de consultas:** Usar **SQLAlchemy con índices** y **consultas eficientes**.

#### ¿Cómo implementarías la paginación en los endpoints que devuelven listas de libros?
- Usar **limit y offset** en las consultas SQL.
- Implementar **FastAPI Query Parameters** (`skip` y `limit`).
- Utilizar **bibliotecas como Pydantic** para definir respuestas paginadas.

#### ¿Cómo asegurarías la seguridad de la aplicación (protección contra inyecciones SQL, XSS, etc.)?
- **Inyección SQL:** Usar **SQLAlchemy ORM** con consultas parametrizadas.
- **XSS y CSRF:** Implementar **CORS** y sanitizar entradas con **Pydantic**.
- **Hashing de contraseñas:** Usar **bcrypt o Argon2**.
- **Validaciones estrictas:** Definir esquemas con **Pydantic y FastAPI Depends**.

 
