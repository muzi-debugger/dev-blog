# DevBlog

DevBlog is a simple blogging platform for developers where users can view posts, write new posts, and manage their own content. This guide walks you through setting up the application, running it locally, and using its features.

---

## Features
- **View Posts**: Browse existing posts, complete with titles, content, and images.
- **Create Posts**: Authenticated users can write and publish their own posts.
- **Responsive Design**: Mobile-friendly interface for seamless browsing.

---

## Prerequisites
- **Python** (version 3.8 or higher)
- **pip** (Python package manager)
- **virtualenv** (optional but recommended for isolated environments)
- **SQLite** (default database, already included with Python)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/devblog.git
cd devblog
```

### 2. Activate a Virtual Environment 
 For Mac/Linux
``` 
python3 -m venv env
source env/bin/activate
```
For Windows
```
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Configure the Database

Run the following commands to create and apply migrations:
```
python manage.py makemigrations
python manage.py migrate
```
### 5. Add a Default Superuser (Optional)

Create a superuser for managing the application through the Django admin panel:
```
python manage.py createsuperuser
```
### 6. Run The Development Server
```python manage.py runserver```
The application will be accessible at: http://127.0.0.1:8000

You can now create an account to create your own posts and view posts. 
Note: You have to be logged in to create your own posts. The purpose of this application is to showcase skills with Django to create a web application






