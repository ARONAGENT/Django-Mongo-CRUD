# Django MongoDB-CRUD Project with Atlas Cloud

This Django project demonstrates MongoDB CRUD (Create, Read, Update, Delete) operations using MongoDB Atlas Cloud.

## Project Overview
This project is designed to manage a collection of workers. It allows users to add, view, update, and delete worker records through a web interface.

### Technologies Used
- **Django** - Web framework for Python
- **MongoDB Atlas** - Cloud database provider
- **PyMongo** - Python driver for MongoDB
- **HTML, CSS, Bootstrap** - Frontend design

---
## Django Project Setup
Follow these steps to set up the Django project on your machine:

### 1. Install Virtual Environment
```sh
pip install virtualenv  # Install virtualenv (one-time installation)
```

### 2. Create and Activate a Virtual Environment
```sh
mkdir django-mongo
cd django-mongo
virtualenv mongoenv  # Create virtual environment
cd mongoenv
cd Scripts
activate  # Start virtual environment
```

### 3. Install Django and PyMongo
```sh
pip install django
pip install pymongo 
```

### 4. Create a Django Project
```sh
django-admin startproject workersWeb
cd workersWeb
```

### 5. Run the Development Server
```sh
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to check if the default Django homepage appears.

### 6. Create Required Directories
```sh
mkdir templates
mkdir static
```

### 7. Configure `settings.py`
Edit `settings.py` to include the following changes:

#### Modify TEMPLATES Section:
```python
'DIRS': [BASE_DIR, "templates"],
```

#### Add Static Files Configuration:
```python
STATICFILES_DIRS = [BASE_DIR, "static"]
```

### 8. Open the Project in VS Code
```sh
code .  # Opens VS Code with the project directory
```

---
## Database Collection (Workers)
This project uses a `worker` collection for CRUD operations. Below is the schema:

```json
{
    "workerid": "integer",
    "name": "string",
    "department": "string",
    "post": "string",
    "salary": "float",
    "location": "string"
}
```

---
## CRUD Operations Performed
This project supports the following operations on the `worker` collection:

1. **Add Worker (INSERT)** - Users can add new workers to the database.
2. **View All Workers (SELECT)** - Displays a list of all workers.
3. **Increment Salary (UPDATE)** - Allows users to increase a worker's salary.
4. **Delete Worker by ID (DELETE)** - Removes a worker record from the database.

---
## Execution ->

https://github.com/user-attachments/assets/b26118af-51f2-421b-9620-dab24978bacd

---
## How to Run the Project
1. Clone this repository:
```sh
git clone https://github.com/ARONAGENT/Django-Mongo-CRUD.git
cd workerWeb
```
2. Activate the virtual environment:
```sh
cd mongoenv
cd Scripts
activate
```
3. Run the Django server:
```sh
python manage.py runserver
```
4. Open `http://127.0.0.1:8000/` in your browser to use the application.

---
## Done!
This completes the setup and execution of the Django MongoDB-CRUD project. 🎉

Feel free to contribute, suggest improvements, or report issues!

