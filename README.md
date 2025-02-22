1 clone repository form github
git clone https://github.com/RashinShan/todo-app.git
cd To_Do_App_Project

2 Install Dependencies
pip install r requirements.txt
3 Set Up Environment Variables
Create a .env file in the root directory and add:
MYSQL_DATABASE=todo_db
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_HOST=localhost
MYSQL_PORT=3306

Running the Django Project
Without Docker
Run the Django development server:
python manage.py runserver
Access the app at http://127.0.0.1:8000/.

With Docker
dockercompose up build d
Access the app at http://localhost:8000/.




Database Migrations
1️ Create Migrations for the App
python manage.py makemigrations To_Do
2️ Apply Migrations
python manage.py migrate

 Running Tests
Run Tests for the To_Do App
python manage.py test To_Do


 Stopping the Project
Without Docker
CTRL + C    Stop the server
With Docker
dockercompose down




