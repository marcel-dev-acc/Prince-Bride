# Prince-Bride: Wedding List Webapp

The files and contents of the files have been created for express purpose of answering the tasks found at the link here https://github.com/prezola/technical-challenge

This is a development project

Pre-requisites:
python 3.8, which can be found here https://www.python.org/

To run this project as a development package:
1) Clone this repository to your machine
2) Install pipenv by running the following command ```pip install pipenv```
3) Navigate to the root folder of this project, which contains the "Pipfile"
4) Execute the command ```pipenv shell```
5) Run ```pip install django```
6) Change the directory to "Prince-Bride", which contains the file: manage.py
7) Execute the command ```python manage.py runserver```

* To access the admin panel, run the command ```python manage.py createsuperuser```
* For database syncing please read the guide here https://docs.djangoproject.com/en/3.0/topics/migrations/

# Prince-Bride: Improvements

These improvements would make the webapp better
1) NGINX to handle multiple concurrent requests
2) User authentication