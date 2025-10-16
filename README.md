# 🚗 DriveHub API – Gestor de Vehículos

## 🧾 Descripción del Proyecto

**DriveHub API** es una aplicación desarrollada con **Django REST Framework (DRF)** que permite gestionar vehículos y sus dueños de manera sencilla y estructurada mediante **endpoints REST**.

Cada vehículo está asociado a un dueño, y el sistema permite realizar todas las operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar) necesarias sobre ambas entidades, además de búsquedas y filtros.

> ❌ **Nota:** No utiliza la interfaz de administración de Django — todas las operaciones se realizan exclusivamente mediante endpoints API.

***

## 🛠️ Tecnologías Utilizadas

* **Python** 3.12+
* **Django** 5.x
* **Django REST Framework (DRF)**
* `django-filter`
* **SQLite3** (por defecto)
* **Git + GitHub**

***

## ⚙️ Instrucciones para Ejecutar el Servidor

Sigue estos pasos para poner en marcha el servidor de desarrollo localmente:

### 1. Clonar el repositorio

git clone [https://github.com/LuisGalvan1512/drivehub_api.git](https://github.com/LuisGalvan1512/drivehub_api.git)
cd drivehub_api

### 2. Crear y activar un entorno virtual

python -m venv venv
# En Windows:
venv\Scripts\activate

# En Linux/Mac:
source venv/bin/activate


### 3. Instalar dependencias

python manage.py makemigrations
python manage.py migrate


### 4. Aplicar migraciones

python manage.py makemigrations
python manage.py migrate


### 5. Ejecutar el servidor

python manage.py runserver


### 6. Probar en el navegador o cliente API

Abre en tu navegador: http://127.0.0.1:8000/api/v1/vehiculos/

O usa un cliente como Postman o Insomnia para interactuar con los endpoints.


###📚 Endpoints Disponibles

🔹 Dueños (/api/v1/duenos/)

Método,Endpoint,Descripción
GET,/api/v1/duenos/,Lista todos los dueños registrados.
POST,/api/v1/duenos/,Crea un nuevo dueño.
GET,/api/v1/duenos/{id}/,Muestra un dueño específico.
PUT / PATCH,/api/v1/duenos/{id}/,Actualiza un dueño.
DELETE,/api/v1/duenos/{id}/,Elimina un dueño.


🔹 Vehículos (/api/v1/vehiculos/)
Método,Endpoint,Descripción
GET,/api/v1/vehiculos/,Lista todos los vehículos.
POST,/api/v1/vehiculos/,Crea un nuevo vehículo (requiere el ID del dueño).
GET,/api/v1/vehiculos/{id}/,Muestra un vehículo específico.
PUT / PATCH,/api/v1/vehiculos/{id}/,Actualiza un vehículo.
DELETE,/api/v1/vehiculos/{id}/,Elimina un vehículo.
GET,/api/v1/vehiculos/?search=Toyota,"Filtra vehículos por marca, modelo o nombre del dueño."

👨‍💻 Autor
Luis Enrique Galván Morales
