Below are the steps I took to deploy the site to Heroku.

## **GitHub/Gitpod**

### **Create Repository**

This project was developed by forking a custom [Code Institute template](https://github.com/Code-Institute-Org/python-essentials-template) which simulates a terminal in the web browser.

- Click the template link above
- Click use this template and create a new respository
- Name the repository
- Launch using the Gitpod web extension

### **Setting up the Workspace**

Below were the steps taken to install the relevant packages to setup django on the workspace using the terminal.

1. Install django using - pip install django==3.2
2. Install gunicorn using - pip install gunicorn
3. Install dj_database_url using - pip install dj_database_url
4. Install psycopg using - pip install psycopg2-binary
5. Create requirements.txt file and freeze installed packages into file using - pip freeze --local > requirements.txt
6. Create django project using - django-admin startproject "your-project-name"
7. Create the first app within the project using - python manage.py startapp "your-app-name"
8. Add the created app to installed apps in the settings.py file
9. Make migrations using - python manage.py makemigrations
10. Migrate the changes using - python manage.py migrate
11. Open up the server to make sure your django project was created successfully using - python manage.py runserver 
  - If the project was created succesfully you will see the django success page.
12. Create env.py file to secure variables you dont want pushed to github.
13. In env.py file create 2 variables
   - 1. os.environ["SECRET_KEY"] = "any-secret-key-you-want"
   - 2. os.environ["DEVELOPMENT"] = "True"
14. Change SECRET_KEY variable in settings.py to - SECRET_KEY = os.environ.get('SECRET_KEY')
15. Change Debug variable in settings.py to -  DEBUG = "DEVELOPMENT" in os.environ
  - With this change debug will be set to True in development and False in production.






