#Nextmotion

The nextmotion Service is responsible for the backend tasks.

### Purpose
*  The nextmotion service manage to all api.

### Generate SSH key
* Run `$ ssh-keygen -t rsa -C "your_email@example.com"`
* Run `$ cat ~/.ssh/id_rsa.pub` and copy ssh key
* Add key in user profile of bit bucket


### Steps to install and run backend on your local machine
* Run `$ pip install virtualenv` command to install virtual environment
* Run `$ virtualenv env -p python3.7` command to Create Virtual environment
* Run `$ source env/bin/activate` command to activate virtual environment
* Run `$ git clone <git url>` command for cloning the project
* Run `$ cd nextmotion` command for jump into the project directory
* Run `$ pip install -r requirements.txt` command to Install project requirement file
* Run `$ python manage.py migrate` command to apply migrations on your local machine
* Run `$ python manage.py runserver` command to run project on your local machine

    
### Running the Tests
* Run `$ cd nextmotion` command for jump into the project directory
* Run `$ python manage.py test` command for run all test cases

### Running Tests Coverage
* Run `$ cd nextmotion` command for jump into the project directory
* Run `$ coverage run --source='.' manage.py test` for run test cases with coverage
* Run `$ coverage html`  to see the result
