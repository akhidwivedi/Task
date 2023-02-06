Test Project(Django Api with custom authentication and custom  permision)

Open command prompt in windows and go inside theth  project folder: mapzot\mapzot>

1.Create a virual environment using the command : python -m venv env
2.Activate virtual Environment using the command : env\Scripts\activate
3.Install all the libraries and dependencies present in requirements.txt using the command : pip install -r requirements.txt
4.Run the project using the command : python manage.py runserver
5.Visit the localhost url on : http://127.0.0.1:8000
6. Follow the endpoints for all tasks.There are two modules  profile and products
7. endpoint: http://127.0.0.1:8000/custom/users/ for  all user related  task.
8. endpoint : http://127.0.0.1:8000/products/ for  product related  task
9. http://127.0.0.1:8000/products/?username=akhil example for  authentication and  according to  the user status  permission is given for  API
10.using the command : python manage.py createsuperuser ,  create  superuser for the  project  to access all the permission
