# slotbooking

This is a simple Booking System webapp made in Django and Angularjs. 

1) Pre-requisites :
- Python 2.7.6

2) Clone the code

2) Install all dependencies:
- Go to the root folder of project and Run following command on LINUX machine:
$ pip install -r requirements.txt

3) Make Database Tables:
$ python manage.py migrate

4) Run application:
$ python manage.py runserver
- This will start this application on http://localhost:8000/

4) Run Test Cases:
$ coverage run manage.py test

5) Check the test coverage:
$ coverage html
- Running the above command will generate a folder named "htmlcov". Open "index.html" in any browser. You will see the code   as well as Test coverage of Django Test Cases. 

