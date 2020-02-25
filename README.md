# inventory management software
A simple inventory management system built with Django.
Users can add stock item and generate bills. All data is stored in database and are rendered in real time

To run project, run the following commands in the project's directory to create the database. When running the software for the first time, it is necessary to run each command for each app in the project
```
python manage.py makemigrations homepage
python manage.py migrate homepage
python manage.py makemigrations inventory
python manage.py migrate inventory
python manage.py makemigrations transactions
python manage.py migrate transactions
```
After the first time, the following can be run to migrate model changes in any app
```
python manage.py makemigrations
python manage.py migrate
```
Use the following command to run the server
```
python manage.py runserver
```
Use the following command to create an admin user 
```
python manage.py createsuperuser
```
