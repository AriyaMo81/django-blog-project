Django Blog Project
A beginner-friendly blog application built with Python and Django. This project demonstrates the fundamentals of building a web application with Django, including templates, models, forms, CRUD operations, user registration, authentication, and Bootstrap styling.
Features
- Display blog posts
- View individual post details
- Create and delete posts
- Reusable templates with Django template inheritance
- Django template tags and filters
- Forms and ModelForms
- User registration
- User login and logout
- Success and error notifications with Django messages
- Conditional navigation based on authentication status
- Bootstrap-based styling
Technologies
- Python
- Django
- SQLite
- HTML and CSS
- Bootstrap
Getting Started
Follow these steps to run the project locally.
1. Clone the repository
git clone <your-repository-url>
cd django-blog-project
Replace <your-repository-url> with the URL of your GitHub repository.
2. Create and activate a virtual environment
Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate.ps1
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
3. Install dependencies
If the project contains a requirements.txt file, install its dependencies:
pip install -r requirements.txt
Otherwise, install Django:
pip install django
4. Apply database migrations
python manage.py migrate
5. Create an administrator account (optional)
python manage.py createsuperuser
6. Start the development server
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser.
Project Structure
The exact structure may vary depending on your local project, but a typical Django project looks like this:
django-blog-project/
├── manage.py
├── db.sqlite3
├── <project_config>/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── blog/
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   └── ...
├── README.md
└── LICENSE
<project_config> represents the Django configuration package. Replace the example app and folder names with the names used in your project.
Learning Goals
This project is intended for practice and learning. It covers the following Django concepts:
- The MVT (Model-View-Template) architecture
- Creating Django projects and applications
- Working with models and the database
- Rendering templates and using template inheritance
- URL routing and named URLs
- Handling forms and validating user input
- Creating, reading, and deleting records
- Registering users and managing authentication
- Displaying messages to users
- Accessing request information in views and templates
Contributing
Suggestions and improvements are welcome. Feel free to fork the repository, make changes, and submit a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for the full license text.