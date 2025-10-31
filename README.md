# 📝 TaskNova - Gestor de Tareas

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3.3-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

> **TaskNova** es una aplicación web moderna para gestión de tareas desarrollada con **Flask**.  
> Ofrece una interfaz intuitiva y características avanzadas para organizar tus actividades diarias.

---

## ✨ Características

✅ **Autenticación segura** – Registro e inicio de sesión  
📋 **CRUD completo de tareas** – Crear, leer, actualizar, eliminar  
🎯 **Sistema de prioridades** – Alta, media, baja  
📊 **Dashboard con estadísticas** – Progreso visual  
🎨 **Temas claro/oscuro** – Personalización de interfaz  
📱 **Diseño responsive** – Compatible con móviles  
⚡ **Filtros y ordenamiento** – Por estado, prioridad y fecha

---

## 🛠️ Tecnologías Utilizadas

### 🔙 Backend
- 🐍 **Python 3.8+** – Lenguaje principal  
- ⚙️ **Flask 2.3.3** – Framework web  
- 🧩 **Flask-SQLAlchemy 3.0.5** – ORM para base de datos  
- 🔐 **Werkzeug 2.3.7** – Seguridad y hashing  
- 🚀 **Gunicorn 21.2.0** – Servidor WSGI para producción  

### 🎨 Frontend
- 🌐 **HTML5** – Estructura semántica  
- 🎨 **CSS3** – Estilos personalizados y responsive  
- 🪶 **Bootstrap 5** – Diseño moderno  

### 🗄️ Base de Datos
- 💾 **SQLite** – Entorno local  
- 🐘 **PostgreSQL** – Producción (Railway)  

### ☁️ Despliegue
- 🧭 **Git & GitHub** – Control de versiones  
- 🚆 **Railway** – Despliegue automático  
- 📦 **pip** – Gestión de dependencias  

---

## 🚀 Instalación Local

### 🔧 Prerrequisitos
- Python 3.8 o superior  
- pip (gestor de paquetes de Python)

### 🪜 Pasos de instalación

```bash
# 1️⃣ Clonar el repositorio
git clone https://github.com/gortizldev-collab/TaskNova.git
cd TaskNova

# 2️⃣ Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# 3️⃣ Instalar dependencias
pip install -r requirements.txt

# 4️⃣ Ejecutar la aplicación
python app.py

# 5️⃣ Abrir en el navegador
# 👉 http://localhost:5000
```
**Luego abre en tu navegador 👉 http://localhost:5000**
### 📁Estructura del Proyecto

```bash
TaskNova/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── Procfile               # Configuración para producción
├── railway.json           # Configuración para Railway
├── .gitignore             # Archivos ignorados por Git
├── README.md              # Documentación
├── templates/             # Plantillas HTML
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── create_task.html
│   └── settings.html
└── static/
    └── css/
        └── style.css
```
### 🖼️ Uso de la Aplicacion
**-Registro:** Crea una cuenta con nombre, email y contraseña

**-Login:** Inicia sesión con tus credenciales

**-Dashboard:** Visualiza tus tareas y progreso

**-Crear Tareas:** Título, descripción, prioridad y fecha límite

**Gestión:** Cambiar estado, filtrar y ordenar

**-Configuración:** Cambiar tema o contraseña
### 👤 Capturas de Pantalla
<img width="1343" height="662" alt="image" src="https://github.com/user-attachments/assets/193d6e56-cd73-4120-8f15-b569790b4c4d" />
<img width="1335" height="649" alt="image" src="https://github.com/user-attachments/assets/46cbffcc-d099-4cd2-af87-dbcb0e54fc28" />
<img width="1279" height="638" alt="image" src="https://github.com/user-attachments/assets/9db95f21-dc6b-4522-8df3-3c3a2aeaf28b" />
<img width="1333" height="642" alt="image" src="https://github.com/user-attachments/assets/0e20d86a-85de-4def-917d-d196dc05edbf" />

### 🤝 Contribuir
Las contribuciones son bienvenidas. Para contribuir:

Fork el proyecto

Crea una rama para tu feature (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add some AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

### Autor
**Gabriel Ortiz Lopez**

-GitHub: @gortizldev-collab

-Proyecto: TaskNova

### 🙏 Agradecimientos
Flask - Framework web minimalista

SQLAlchemy - ORM para Python

Bootstrap - Inspiración para diseño

Railway - Plataforma de despliegue
