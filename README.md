# Books API - Backend FastAPI

API RESTful para gestión de libros construida con FastAPI y PostgreSQL usando Docker.

## 📋 Prerrequisitos

### Lo que necesitas instalar:

| Herramienta | Linux | Windows |
|-------------|-------|---------|
| Docker | `sudo apt update && sudo apt install docker.io` (Ubuntu/Debian) | [Docker Desktop](https://www.docker.com/products/docker-desktop/) |
| Docker Compose | Incluido en Docker Desktop / `sudo apt install docker-compose-v2` | Incluido en Docker Desktop |

### Verificar instalación:
```bash
# Linux/Windows (PowerShell/CMD)
docker --version
docker compose version
```

---

## 🚀 Cómo levantar los contenedores

### Linux:
```bash
# 1. Navegar al directorio del backend
cd /home/jdlo/Documentos/proyectos/pruebasPython/backendPython

# 2. Levantar contenedores en segundo plano
docker compose up -d

# 3. Ver logs (opcional)
docker compose logs -f web

# 4. Ver estado de contenedores
docker compose ps
```

### Windows (PowerShell/CMD):
```powershell
# 1. Navegar al directorio del backend
cd C:\ruta\a\backendPython

# 2. Levantar contenedores en segundo plano
docker compose up -d

# 3. Ver logs (opcional)
docker compose logs -f web

# 4. Ver estado de contenedores
docker compose ps
```

---

## 🌐 Acceso a la API

| Servicio | URL | Descripción |
|----------|-----|-------------|
| FastAPI | http://localhost:8000 | API principal |
| Documentación Swagger | http://localhost:8000/docs | Interfaz interactiva |
| PostgreSQL | localhost:5432 | Base de datos |

---

## 📚 Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/books` | Listar todos los libros |
| GET | `/api/books/{id}` | Obtener libro por ID |
| POST | `/api/books` | Crear nuevo libro |
| PUT | `/api/books/{id}` | Actualizar libro |
| DELETE | `/api/books/{id}` | Eliminar libro |

### Ejemplo de JSON para crear libro:
```json
{
  "title": "Clean Code",
  "author": "Robert C. Martin",
  "year": 2008,
  "isbn": "978-0132350884",
  "publisher": "Prentice Hall",
  "pages": 431,
  "genre": "Programming",
  "description": "A handbook of agile software craftsmanship"
}
```

---

## ⚙️ Configuración

### Variables de entorno (.env):
```
DATABASE_URL=postgresql://books_user:books_password@db:5432/books_db
```

### Servicios Docker:
- **db**: PostgreSQL 15 con healthcheck
- **web**: FastAPI con recarga automática (--reload)

---

## 🛑 Cómo detener los contenedores

### Linux/Windows:
```bash
# Detener contenedores (mantiene volúmenes)
docker compose down

# Detener y eliminar volúmenes (borra datos de la BD)
docker compose down -v
```

---

## 📦 Estructura del proyecto
```
backendPython/
├── docker-compose.yml    # Orquestación de contenedores
├── Dockerfile            # Imagen FastAPI
├── .env                  # Variables de entorno
├── requirements.txt       # Dependencias Python
├── main.py               # Entrada de la aplicación
├── database.py           # Configuración SQLAlchemy
├── models.py             # Modelo de datos
├── schemas.py            # Esquemas Pydantic
├── crud.py               # Operaciones CRUD
└── routers/
    └── books.py          # Endpoints de la API
```

---

## 🔧 Comandos útiles

```bash
# Reconstruir imágenes después de cambios
docker compose up -d --build

# Entrar al contenedor de la base de datos
docker compose exec db psql -U books_user books_db

# Ver logs en tiempo real
docker compose logs -f

# Listar contenedores corriendo
docker ps
```
