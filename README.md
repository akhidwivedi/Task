# Task

Test Project(Django Api with custom authentication and custom  permision)

Open command prompt in windows and go inside theth  project folder: mapzot\mapzot>

Create a virual environment using the command : python -m venv env
Activate virtual Environment using the command : env\Scripts\activate
Install all the libraries and dependencies present in requirements.txt using the command : pip install -r requirements.txt
Run the project using the command : python manage.py runserver
Visit the localhost url on : http://127.0.0.1:8000
Follow the endpoints for all tasks.There are two modules  profile and products
endpoint: http://127.0.0.1:8000/custom/users/ for  all user related  task.
endpoint : http://127.0.0.1:8000/products/ for  product related  task
http://127.0.0.1:8000/products/?username=akhil example for  authentication and  according to  the user status  permission is given for  API
using the command : python manage.py createsuperuser ,  create  superuser for the  project  to access all the permission
