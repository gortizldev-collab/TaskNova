#Importamos todo lo que se necesita para este proyecto a continuacion le digo para que sirve cada dependencia o libreria
#Importamos el framework de flask y de flask importamos lo siguiente:
#'render_template' este sirve para renderizar nuestra respuesta html apartir de una plantilla y datos que trabajaremos con flask
#'request' sirve para poder hacer una peticion o solicitud esta es ideal cuando se trabaja con apis
#'url_for' no es mas que para generar URLs dinamicas con algunos parametros que se le proporciona
#'flash' sirve para generar mensajes temporales en nuestra app web
#De flask_sqlalchemy importamos SQLAlchemy esto es un ORM que nos ayuda a interatuar mejor con nuestra base datos en py
#datetime nos ayuda proporcionando la fecha y hora actual
#werkzeug.security nos ayuda generando hash de las contraseñas ingresadas y tambien para chekearlas
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from dotenv import load_dotenv
#creamos una instancia del framework y la asignamos a la variable app
#empezamos a configurarla, esta tendra una llave secreta
#le decimos que SQLALCHEMY_DATABASE_URI va a hacer 'sqlite:///database.db' esta es nuestra base de datos si no existe se crea automaticamente cuando se ejecute
#lo ultimo es mas que todo para disminuir el consumo de memoria ya que no necesitamos el seguimiento de modificaciones
load_dotenv()  # 🔹 Carga las variables del archivo .env
app = Flask(__name__)
app.config['SECRET_KEY'] = 'tasknova-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#aca asignamos a la variable db el SQLAlchemy(app) esta sera la variable con que trabajaremos nuestra base de datos
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Modelos
#Creamos nuestra primera tabla con nombre 'users'
#dentro de esta tabla trabajaremos con las sguientes columnas que almanceran los datos las columnas estar proporcionda como lo siguiente:
#id que sera un valor entero y tendra una primary_key
#name esta sera de tipo string que tendra una capacidad maxima de 100 caracteres y el campo no puede estar vacio 
#email que sera tambien de tipo string con una capacidad maxima de 100 este correo debe ser unico y no puede estar el campo vacio 
#password sera un string de maximo 200 caracteres se trabaja con este valor alto ya que recuerda que las contraseñas trabajan con hash y estas por lo general son largas y el campo no puede ser vacio 
# tema que por default esta en claro
#taskt que tiene una relationship ya que un usuario puede tener varias tareas guardadas
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) #id unico
    name = db.Column(db.String(100), nullable=False) #name obligatorio
    email = db.Column(db.String(100), unique=True, nullable=False)#email obligatorio
    password = db.Column(db.String(200), nullable=False)#password obligatorio
    theme = db.Column(db.String(10), default='light')# Tema de interfaz (claro/oscuro)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)#fecha de creacion automatica
    
    tasks = db.relationship('Task', backref='user', lazy=True)# Relación uno-a-muchos: Un usuario puede tener muchas tareas

#Creamos la segunda tabla 'Task'
#Tambien tendra un id 
#Titulo de la tarea que sera de tipo string con un maximo de 100 caracteres y no podra estar vacio ese campo 
#En la desripcion sera de tipo texto pero esta si puede quedar vacia
#para obetner la fecha y hora utilizamos el datetime
#status que por default es pendiente
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.DateTime)
    priority = db.Column(db.String(20), default='media')# Prioridad: baja, media, alta
    status = db.Column(db.String(20), default='pendiente')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# Rutas de Autenticación
# Definimos los endpoints y la lógica de cada página
@app.route('/') 
#Ruta principal de la aplicación
#Redirige al dashboard si el usuario está logueado
#o al login si no hay sesión activa
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
#Ruta para iniciar sesión
#GET: Muestra el formulario de login
#POST: Procesa los datos del formulario y autentica al usuario
def login():
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        email = request.form['email']
        password = request.form['password']
        remember = 'remember' in request.form
        # Buscamos el usuario en la base de datos
        user = User.query.filter_by(email=email).first()
        # Verificamos si el usuario existe y la contraseña es correcta
        if user and check_password_hash(user.password, password):
            # Guardamos la información en la sesión
            session['user_id'] = user.id
            session['user_name'] = user.name
            session['theme'] = user.theme
            # Si marcó "Recordarme", hacemos la sesión permanente
            if remember:
                session.permanent = True
                
            flash('¡Bienvenido de nuevo!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Correo o contraseña incorrectos', 'error')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    #Ruta para registrar nuevos usuarios
    #GET: Muestra el formulario de registro
    #POST: Procesa los datos y crea el nuevo usuario
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        # Verificamos si el email ya está registrado
        if User.query.filter_by(email=email).first():
            flash('Este correo ya está registrado', 'error')
            return render_template('register.html')
        # Hasheamos la contraseña por seguridad
        hashed_password = generate_password_hash(password)
        # Creamos el nuevo usuario
        new_user = User(name=name, email=email, password=hashed_password)
        # Guardamos en la base de datos
        db.session.add(new_user)
        db.session.commit()
        
        flash('¡Cuenta creada exitosamente! Ahora inicia sesión', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/logout')
def logout():
    #Ruta para cerrar sesión
    #Limpia toda la información de la sesión
    session.clear()
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('login'))

# Rutas de la Aplicación
@app.route('/dashboard')
def dashboard():
    #Ruta principal después del login
    #Muestra el dashboard con las tareas del usuario
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    # Obtenemos el usuario actual y sus tareas
    user = User.query.get(session['user_id'])
    tasks = Task.query.filter_by(user_id=user.id).all()
    # Filtramos tareas por estado para las estadísticas
    completed_tasks = [task for task in tasks if task.status == 'completada']
    pending_tasks = [task for task in tasks if task.status == 'pendiente']
    
    return render_template('dashboard.html', 
                         user=user,
                         tasks=tasks,
                         completed_tasks=completed_tasks,
                         pending_tasks=pending_tasks)

@app.route('/create-task', methods=['GET', 'POST'])
def create_task():
    #Ruta para crear nuevas tareas
    #GET: Muestra el formulario de creación
    #POST: Procesa los datos y crea la nueva tarea
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        #Obtenemos los datos del formulario
        title = request.form['title']
        description = request.form['description']
        due_date_str = request.form['due_date']
        priority = request.form['priority']
        
        # Convertimos la fecha de string a objeto datetime
        due_date = None
        if due_date_str:
            due_date = datetime.strptime(due_date_str, '%Y-%m-%d')
        
        # Creamos la nueva tarea
        new_task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
            user_id=session['user_id']
        )
        
        # Guardamos en la base de datos
        db.session.add(new_task)
        db.session.commit()
        
        flash('¡Tarea creada exitosamente!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('create_task.html')

@app.route('/update-task-status/<int:task_id>/<status>')
#Ruta para actualizar el estado de una tarea
#Ej: Marcar como completada, poner en progreso, etc.
def update_task_status(task_id, status):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()
    if task:
        task.status = status
        db.session.commit()
        flash('Estado de tarea actualizado', 'success')
    
    return redirect(url_for('dashboard'))

@app.route('/delete-task/<int:task_id>')
def delete_task(task_id):
    # Ruta para eliminar una tarea
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
     # Buscamos la tarea (solo si pertenece al usuario actual)
    task = Task.query.filter_by(id=task_id, user_id=session['user_id']).first()
    if task:
        db.session.delete(task)
        db.session.commit()
        flash('Tarea eliminada', 'info')
    
    return redirect(url_for('dashboard'))

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    # Ruta para la configuración del usuario
    #GET: Muestra el formulario de configuración
    #POST: Actualiza la información del usuario
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    
    if request.method == 'POST':
        # Actualizamos los datos del usuario
        user.name = request.form['name']
        user.email = request.form['email']
        user.theme = request.form['theme']
        
        # Solo actualizamos la contraseña si se proporcionó una nueva
        if request.form['password']:
            user.password = generate_password_hash(request.form['password'])
        
        db.session.commit()

        # Actualizamos la sesión con los nuevos datos
        session['user_name'] = user.name
        session['theme'] = user.theme
        
        flash('Configuración actualizada', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('settings.html', user=user)

# INICIALIZACIÓN DE LA APLICACIÓN
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    # Configuración para producción
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)