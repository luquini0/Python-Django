# Proyecto: Python-Django

Descripción
-----------

Este es un proyecto de ejemplo creado con Django que contiene una pequeña aplicación para listar y comprar perros. Está pensado como ejercicio práctico del curso de CoderHouse y contiene:

- Una app llamada `inicio` con vistas y plantillas para listar y comprar perros.
- El proyecto Django principal en la carpeta `seguimiento` con la configuración del proyecto.
- Base de datos SQLite local (`db.sqlite3`) y migraciones iniciales.

Requisitos
----------

- Python 3.10+ (o la versión compatible del entorno).
- pip
- Dependencias listadas en `requirements.txt` (instálalas con pip).

Instalación (Windows - PowerShell)
---------------------------------

1. Clona o descarga el repositorio y sitúate en la carpeta del proyecto:

```powershell
cd "c:\Users\cread\OneDrive\Documentos\Cursos CoderHouse\78335\clases-78335-main\proyecto"
```

2. (Opcional pero recomendado) Crea y activa un entorno virtual:

```powershell
python -m venv .venv
\.venv\Scripts\Activate.ps1
# Si PowerShell bloquea la ejecución, permitir scripts para el usuario:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Instala dependencias:

```powershell
pip install -r requirements.txt
```

4. Aplica migraciones y crea un superusuario si lo necesitas:

```powershell
python manage.py migrate
python manage.py createsuperuser
```

Uso (levantar servidor de desarrollo)
------------------------------------

```powershell
python manage.py runserver
# Luego abre http://127.0.0.1:8000/ en tu navegador
```

Estructura del proyecto (resumen)
---------------------------------

- `manage.py` - utilidades de administración de Django.
- `db.sqlite3` - base de datos SQLite usada localmente.
- `requirements.txt` - dependencias del proyecto.
- `seguimiento/` - paquete del proyecto Django (settings, urls, wsgi/asgi).
- `inicio/` - app principal con modelos, vistas y plantillas (`templates/`).
- `templates/` - plantillas globales del proyecto (p. ej. `inicio.html`, `listar_perros.html`).

Tareas comunes
--------------

- Ejecutar tests:

```powershell
python manage.py test
```

- Crear migraciones cuando modifiques modelos:

```powershell
python manage.py makemigrations
python manage.py migrate
```


# How To

1. path('comprar-perro/<raza>/<tamaño>', comprar_perro)

Esta línea define una ruta (URL) en Django, que permite crear/agregar un perro directamente desde la URL.

Qué significa cada parte:

path(...) → función de Django que registra una nueva URL.

'comprar-perro/<raza>/<tamaño>' → la dirección que el usuario visita.

<raza> y <tamaño> son parámetros dinámicos, es decir, Django va a capturar los valores que se escriban ahí.

Ejemplo:

http://localhost:8000/comprar-perro/Labrador/Grande


→ Django tomará raza = "Labrador" y tamaño = "Grande".

comprar_perro → el nombre de la vista (la función en views.py) que se ejecuta cuando alguien entra a esa URL.

Qué hace la vista comprar_perro:

def comprar_perro(request, raza, tamaño):
    perro = Perro(raza=raza, tamaño=tamaño)
    perro.save()
    return render(request, 'comprar_perro.html', {'perros_comprados': perro})


Crea un nuevo objeto Perro con los datos de la URL.

Lo guarda en la base de datos (perro.save()).

Muestra una página (template comprar_perro.html) confirmando el registro.

En resumen:

Esta ruta sirve para agregar perros al sistema directamente desde la URL.

2. path('listar-perros/', listar_perros)

Esta define la ruta donde se listan todos los perros guardados en la base de datos.

Qué significa:

'listar-perros/' → cuando el usuario entra a esta URL, se muestra la lista de todos los perros.

Ejemplo:

http://localhost:8000/listar-perros/


listar_perros → es la vista encargada de obtener todos los perros del modelo Perro y pasarlos al template.

La vista:

def listar_perros(request):
    perros = Perro.objects.all()
    return render(request, 'listar_perros.html', {'listado_de_perros': perros})


Recupera todos los perros (Perro.objects.all()) desde la base de datos.

Muestra el template listar_perros.html, enviándole la lista como variable listado_de_perros.

En resumen:

Esta ruta sirve para ver todos los perros comprados o registrados.

Ejemplo visual del flujo completo:
Acción	URL	Qué hace
Agregar perro	/comprar-perro/Labrador/Grande	Crea un nuevo perro (raza Labrador, tamaño Grande)
Ver lista	/listar-perros/	Muestra todos los perros guardados
