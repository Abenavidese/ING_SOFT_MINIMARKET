## MiniMarket API - Sistema de Gestión Backend

Este proyecto es un backend desarrollado con **FastAPI**, que permite gestionar entidades claves de un minimarket como ventas, productos, proveedores, clientes, y más. Utiliza SQLAlchemy como ORM, Pydantic para validaciones, y puede conectarse a PostgreSQL o SQLite.

---

## 📂 Estructura del Proyecto

```text
mini_market/
|
└──app/
|    ├── controllers/ # Rutas (endpoints de la API)
|    ├── models/ # Modelos de base de datos con SQLAlchemy
|    ├── schemas/ # Esquemas de validación Pydantic
|    ├── services/ # Lógica de negocio
|    ├── repositories/ # Acceso a datos (consultas SQL)
|    ├── config/ # Configuración de la base de datos
|
└── requirements.txt #Archivo con los requerimientos de la aplicacion
└── README.md # Manual de uso de la aplicacion
└── minimarket.db #Archivo local con la base de datos
└── .gitignore #Archivo para ignorar archivos que no se desean subir
└── .env #Variables de entorno
└── main.py # Punto de entrada de la aplicación
```


---

##  Funcionalidades Implementadas

### CRUDs Activos

- [x] **Categorias**
- [x] **Cajas** 
- [x] **Clientes**
- [x] **Productos**
- [x] **Ventas**
- [x] **Detalles de Venta**
- [x] **Proveedores**

Cada entidad incluye:
- Crear (`POST`)
- Listar todos (`GET`)
- Buscar por ID (`GET /{id}`)
- Actualizar (`PUT`)
- Eliminar (`DELETE`)

---

## Tecnologías Usadas

- [FastAPI](https://fastapi.tiangolo.com/) – Framework web moderno
- [SQLAlchemy](https://www.sqlalchemy.org/) – ORM para manejo de base de datos
- [Pydantic](https://docs.pydantic.dev/) – Validación de datos
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI para FastAPI
- [SQLite/PostgreSQL] – Bases de datos soportadas

---

## Configuración y Ejecución

### 1. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 2. Configurar la base de datos
En app/config/database.py configura tu motor de base de datos:

```bash
DATABASE_URL = "sqlite:///./db.sqlite3"
# o para PostgreSQL:
# DATABASE_URL = "postgresql://usuario:contraseña@localhost:5432/tu_db"
```

### 3. Ejecutar servidor

```bash
uvicorn app.main:app --reload
```

### 4. Documentación Swagger

Una vez el servidor este corriendo ingresar a:

```bash
http://localhost:8000/docs
```


## Ejmplo de uso


Crear un proveedor

```bash
POST /proveedores/
{
  "nombre": "Distribuidora Central",
  "telefono": "0987654321",
  "email": "proveedor@central.com"
}
```


Actualizar una venta

```bash
PUT /ventas/1
{
  "fecha": "2024-06-01",
  "total": 45.00,
  "cliente_id": 2
}
```

### Recomendaciones

- Usa SQLite para desarrollo y PostgreSQL para producción.

- Configura variables de entorno para evitar hardcodear credenciales.

- Agrega autenticación con JWT para mayor seguridad si se conecta a frontend.

### Frontend - Aplicación Web Angular
El frontend está desarrollado en Angular y consume la API REST del backend para gestionar todas las entidades del minimarket. Proporciona una interfaz amigable y funcional para los usuarios finales.

Funcionalidades principales
  - Gestión completa de:
    - Categorías
    - Cajas
    - Clientes
    - Productos
    - Ventas y detalles de venta
    - Proveedores

  - Formularios validados para creación y actualización.
  - Visualización de listas con paginación y búsqueda.
  - Comunicación asíncrona con el backend mediante HTTPClient.
  - Manejo básico de estados y errores en la interfaz.
  - Navegación y diseño responsivo para mejor experiencia.

```text
mini_market/
|
└──app/FRONTEND/minimarket-front/
|    ├── components/      # Componentes reutilizables y vistas
│    ├── services/        # Servicios para llamadas API
│    ├── app-routing.module.ts  # Configuración de rutas
│    └── app.module.ts    # Módulo principal
└── package.json             # Dependencias del frontend
```

### Instalación y Ejecución
  
  1. Instalar dependencias:
  
  ```bash
  cd front-end
  npm install
  ```

  2. Ejecutar el servidor de desarrollo:

  ```bash
  ng serve --open
  ```

  3. La aplicación se abrirá en el navegador en

  ```bash
  http://localhost:4200.
  ```

### Interfaz de Usuario

- Formularios con validaciones para evitar errores de entrada.
- Listados con paginación, búsqueda y filtros para facilitar la navegación.
- Mensajes de error y confirmación para mejorar la experiencia del usuario.
- Navegación fluida entre vistas mediante rutas configuradas en Angular Router.
- Diseño responsivo para uso en dispositivos móviles y de escritorio.
  
### Autores


- Anthony Alexander Benavides Erique
- Bryam Jesus Peralta Navarro
- Erick Fernando Zhigue Granda
- Henry Augusto Granda Lopez 























