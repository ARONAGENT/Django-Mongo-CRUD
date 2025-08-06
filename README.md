# Django MongoDB-CRUD Project with Atlas Cloud

[![Django](https://img.shields.io/badge/Django-5.x-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-7.x-green.svg)](https://www.mongodb.com/)
[![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-Cloud-brightgreen.svg)](https://www.mongodb.com/atlas)
[![PyMongo](https://img.shields.io/badge/PyMongo-4.x-orange.svg)](https://pymongo.readthedocs.io/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.x-blueviolet.svg)](https://getbootstrap.com/)
[![NoSQL](https://img.shields.io/badge/NoSQL-Database-red.svg)](https://en.wikipedia.org/wiki/NoSQL)

## 📋 Project Overview

This Django web application demonstrates comprehensive MongoDB CRUD (Create, Read, Update, Delete) operations using **MongoDB Atlas Cloud**. The project focuses on managing a worker database with a modern NoSQL approach, showcasing the integration between Django and MongoDB through PyMongo driver.

## 👨‍💼 Demo Video

https://github.com/user-attachments/assets/b26118af-51f2-421b-9620-dab24978bacd

*Watch the complete demonstration of MongoDB CRUD operations in action!*

## ✨ Features

### Core Functionality
- 👨‍💼 **Add New Workers** - Insert worker records with complete details
- 📖 **View All Workers** - Display comprehensive worker catalog
- 💰 **Increment Salary** - Update worker salary with increment functionality
- 🗑️ **Delete Workers** - Remove workers by ID
- 📱 **Responsive Design** - Mobile-friendly interface with Bootstrap

### Technical Features
- **MongoDB Atlas Integration** - Cloud-hosted NoSQL database
- **PyMongo Driver** - Efficient Python-MongoDB connectivity
- **Document-based Storage** - Flexible JSON-like document structure
- **Bootstrap UI** - Modern and responsive design
- **Error Handling** - Robust validation and error management
- **NoSQL Operations** - Native MongoDB query operations

## 🛠️ Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Django** | 5.x | Web Framework |
| **Python** | 3.x | Backend Language |
| **MongoDB** | 7.x | NoSQL Database |
| **MongoDB Atlas** | Cloud | Database Hosting |
| **PyMongo** | 4.x | MongoDB Python Driver |
| **HTML5** | Latest | Markup |
| **CSS3** | Latest | Styling |
| **Bootstrap** | 5.x | UI Framework |

## 🗄️ Database Schema

### Workers Collection Structure
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

### Document Example
```json
{
    "_id": ObjectId("507f1f77bcf86cd799439011"),
    "workerid": 1001,
    "name": "John Smith",
    "department": "Engineering",
    "post": "Software Developer",
    "salary": 75000.0,
    "location": "New York"
}
```

### Field Descriptions
| Field | Type | Description |
|-------|------|-------------|
| `_id` | ObjectId | MongoDB unique identifier (auto-generated) |
| `workerid` | Integer | Custom worker identification number |
| `name` | String | Worker's full name |
| `department` | String | Department/division |
| `post` | String | Job title/position |
| `salary` | Float | Current salary amount |
| `location` | String | Work location/office |

## 🔧 CRUD Operations

### 1. **CREATE** - Add New Worker
- Form-based worker entry
- Document insertion into MongoDB collection
- Auto-generated ObjectId and custom worker ID

### 2. **READ** - View Workers
- **View All Workers** - Complete worker catalog display
- **MongoDB Aggregation** - Advanced querying capabilities
- **Document Retrieval** - Efficient cursor-based operations

### 3. **UPDATE** - Modify Worker Records  
- **Increment Salary** - Salary increment functionality
- **Document Updates** - Atomic update operations
- **Field Modifications** - Selective field updates

### 4. **DELETE** - Remove Worker Records
- **Delete by Worker ID** - Remove specific workers
- **Document Deletion** - Complete record removal
- **Confirmation Dialogs** - Prevent accidental deletions

## 🚀 Installation & Setup

### Prerequisites

Ensure you have the following installed:
- **Python 3.8+**
- **pip** (Python package manager)
- **Git**
- **MongoDB Atlas Account** (Free tier available)
- **Code Editor** (VS Code recommended)

### Step-by-Step Installation

#### 1. **Setup Virtual Environment**
```bash
# Install virtualenv (one-time setup)
pip install virtualenv

# Create project directory
mkdir django-mongo
cd django-mongo

# Create virtual environment
virtualenv mongoenv
cd mongoenv

# Activate virtual environment
# On Windows:
cd Scripts
activate

# On macOS/Linux:
source bin/activate
```

#### 2. **Install Dependencies**
```bash
# Install Django and MongoDB driver
pip install django
pip install pymongo
pip install dnspython  # For MongoDB Atlas connection
```

#### 3. **Clone & Setup Project**
```bash
# Clone the repository
git clone https://github.com/ARONAGENT/Django-Mongo-CRUD.git
cd Django-Mongo-CRUD

# Create Django project structure (if starting fresh)
django-admin startproject workersWeb
cd workersWeb

# Create required directories
mkdir templates
mkdir static
```
#### 4. **Run Development Server**
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to access the application.

## 📁 Project Structure


<img width="377" height="701" alt="image" src="https://github.com/user-attachments/assets/0a413ffb-b287-42d7-b5c4-18baf868f33b" />



## 🔗 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home page with workers list |
| `GET` | `/add/` | Add new worker form |
| `POST` | `/add/` | Create new worker |
| `GET` | `/increment/<int:id>/` | Salary increment form |
| `POST` | `/increment/<int:id>/` | Update worker salary |
| `POST` | `/delete/<int:id>/` | Delete worker record |

## ☁️ MongoDB Atlas Configuration

### Setting up MongoDB Atlas

1. **Create MongoDB Atlas Account**
   - Visit [MongoDB Atlas](https://www.mongodb.com/atlas)
   - Sign up for a free account (512MB free tier)

2. **Create Cluster**
   - Choose cloud provider (AWS/GCP/Azure)
   - Select region closest to your location
   - Choose M0 Sandbox (free tier)

3. **Configure Database Access**
   ```
   Database Access → Add New Database User
   Username: your-username
   Password: your-secure-password
   Database User Privileges: Read and write to any database
   ```

4. **Configure Network Access**
   ```
   Network Access → Add IP Address
   Access List Entry: 0.0.0.0/0 (Allow access from anywhere)
   Or add your specific IP address for security
   ```

5. **Get Connection String**
   ```
   Clusters → Connect → Connect your application
   Copy connection string:
   mongodb+srv://<username>:<password>@cluster0.xxxxx.mongodb.net/<dbname>?retryWrites=true&w=majority
   ```

### MongoDB Operations Examples

#### Inserting Documents
```python
# Insert single worker
worker_data = {
    'workerid': 1001,
    'name': 'John Doe',
    'department': 'Engineering',
    'post': 'Software Developer',
    'salary': 75000.0,
    'location': 'New York'
}
collection.insert_one(worker_data)

# Insert multiple workers
workers_data = [
    {'workerid': 1002, 'name': 'Jane Smith', 'department': 'HR'},
    {'workerid': 1003, 'name': 'Bob Johnson', 'department': 'Finance'}
]
collection.insert_many(workers_data)
```

#### Querying Documents
```python
# Find all workers
all_workers = collection.find({})

# Find workers by department
eng_workers = collection.find({'department': 'Engineering'})

# Find workers with salary > 70000
high_salary_workers = collection.find({'salary': {'$gt': 70000}})

# Find single worker by ID
worker = collection.find_one({'workerid': 1001})
```

#### Updating Documents
```python
# Update single field
collection.update_one(
    {'workerid': 1001},
    {'$set': {'salary': 80000}}
)

# Increment salary
collection.update_one(
    {'workerid': 1001},
    {'$inc': {'salary': 5000}}
)

# Update multiple fields
collection.update_one(
    {'workerid': 1001},
    {'$set': {'post': 'Senior Developer', 'salary': 85000}}
)
```

#### Deleting Documents
```python
# Delete single worker
collection.delete_one({'workerid': 1001})

# Delete multiple workers
collection.delete_many({'department': 'Temp'})
```



## 👥 Authors & Contributors

- **[ARONAGENT](https://github.com/ARONAGENT)** - Project Creator & Maintainer

## 🙏 Acknowledgments

- **Django Community** - For the excellent web framework
- **MongoDB Team** - For the powerful NoSQL database
- **MongoDB Atlas** - For reliable cloud database hosting
- **PyMongo Team** - For the excellent Python driver
- **Bootstrap Team** - For the responsive UI framework
- **Open Source Community** - For continuous inspiration and support

## 📞 Support & Contact

### Getting Help
- 📖 **Documentation**: Check this README first
- 🐛 **Bug Reports**: [Create an Issue](https://github.com/ARONAGENT/Django-Mongo-CRUD/issues)
- 💡 **Feature Requests**: [Suggest Features](https://github.com/ARONAGENT/Django-Mongo-CRUD/issues)
- 💬 **Questions**: [Start a Discussion](https://github.com/ARONAGENT/Django-Mongo-CRUD/discussions)

### Connect with the Developer
- **GitHub**: [@ARONAGENT](https://github.com/ARONAGENT)
- **LinkedIn**: [Connect for professional inquiries]
- **Email**: [Contact via GitHub]

## 📊 MongoDB vs SQL Comparison

| Feature | MongoDB | Traditional SQL |
|---------|---------|-----------------|
| **Data Model** | Document-based | Table-based |
| **Schema** | Flexible/Dynamic | Fixed/Rigid |
| **Scalability** | Horizontal | Vertical |
| **Query Language** | MongoDB Query Language | SQL |
| **Transactions** | Limited ACID | Full ACID |
| **Relationships** | Embedded/Referenced | Foreign Keys |

---

⭐ **If you find this project helpful, please give it a star!** ⭐

*Built with ❤️ using Django, MongoDB Atlas, and modern NoSQL practices*
