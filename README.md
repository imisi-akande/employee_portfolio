# employee_portfolio
## Description
In this repository I created an employee portfolio API. This can help employers to manage their employees profile.
This API should therefore help employers to create and manage employees information.

The API should have the ability to:

Create a Department
Retrieve a Department
Update a Department
And, Delete Department(CRUD)
Authentication of API Users
Searching Departments
Adding employees to the department

## Run the Notebook

#### Install pip On Windows
- python -m pip install -U pip setuptools

#### Install/Upgrade pip On OS X or Linux
- sudo easy_install pip
- pip install -U pip setuptools

#### Install virtualenv and create a virtual environment
pip install virtualenv

virtualenv -p python3 envname

#### Activate the environment
source envname/bin/activate

#### Install Jupyter 
- pip3 install jupyter

#### To Run: 
> cd into employee_portfolio.
> run python manage.py migrate
> python manage.py createsuperuser  - To create users
> python manage.py runserver   - To run the app

