# 🛒 Gestor de Productos con MySQL - Zionbyte

Aplicación de consola CRUD (Crear, Leer, Actualizar, Eliminar) para la gestión de productos de una tienda o panadería.  
Desarrollada en Python, con persistencia de datos en una base de datos MySQL.

Este proyecto busca ser una práctica completa e integrada de programación estructurada, manejo de bases de datos y organización de código modular.

---

## 🚀 Funcionalidades

- Crear productos con nombre, descripción, categoría y precio.
- Ver productos por nombre, categoría o rango de precio.
- Actualizar productos individualmente o por campo.
- Eliminar productos de forma segura con confirmación.
- Interfaz de consola con menú interactivo y navegación intuitiva.

---

## 🛠️ Tecnologías utilizadas

- Python 3.11.4
- MySQL (motor de base de datos relacional)
- mysql-connector-python (librería para conectar Python con MySQL)

---

## 🧱 Estructura del proyecto

gestor_productos/
│
├── main.py               # Menú principal de navegación
├── db.py                 # Conexión a la base de datos y ejecución de queries
├── utils.py              # Funciones auxiliares comunes (validaciones, helpers)
│
├── create.py              # Lógica para crear productos
├── read.py                # Lógica para buscar y visualizar productos
├── update.py         # Lógica para actualizar productos
├── delete.py           # Lógica para eliminar productos
│
├── database/
│   └── init.sql          # Script para crear la base de datos y la tabla productos
│
├── README.md             # Este archivo de documentación
└── requirements.txt      # Dependencias del proyecto (opcional)

---

## 🧾 Modelo de Datos

La tabla `productos` tiene la siguiente estructura:

```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(50),
    precio DECIMAL(10,2) NOT NULL
);



⸻

📦 Instalación y uso
	1.	Clona este repositorio:

git clone https://github.com/tu_usuario/gestor_productos.git
cd gestor_productos

	2.	Crea la base de datos y tabla ejecutando el script:

mysql -u tu_usuario -p < database/init.sql

	3.	Instala dependencias (si usás requirements.txt):

pip install -r requirements.txt

	4.	Ejecuta la aplicación:

python main.py



⸻
## ✨ Objetivo educativo

Este proyecto fue desarrollado como práctica personal para reforzar habilidades en:

- Diseño y desarrollo de CRUD reales con conexión a base de datos.
- Organización modular de código en Python.
- Uso efectivo de MySQL para almacenamiento y consultas.
- Buenas prácticas de programación estructurada.
- Pensamiento lógico aplicado al desarrollo de software.

Forma parte del camino de aprendizaje de **Zionbyte**, una marca personal enfocada en construir herramientas digitales con propósito, calidad y evolución constante.

---

## 📌 Recomendaciones

- Asegúrate de tener un servidor MySQL en ejecución.
- Modifica los parámetros de conexión en `db.py` para adaptarlos a tu entorno.
- Practica extendiendo la lógica con validaciones, logs o exportaciones si deseas mejorar el proyecto.

---

