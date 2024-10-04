This smart healthcare application offers seamless communication between users and clinicians, allowing users to search for disease symptoms anytime, anywhere. The software makes online consultations more efficient by offering a user-friendly interface for rapid access to symptom information and healthcare resources.

Features
Look for symptoms and get information about illnesses.
Through the site, users may simply communicate with doctors.
Physicians are qualified to administer patient data and offer medical guidance.
Doctors and users alike can register and log in securely.
Effective backend system for handling medical records and patient data.
Technologies Used
Frontend: HTML, CSS, JavaScript
Backend: Django
Database: MySQL

Setup and Installation
To run this project locally:

Clone the repository:
git clone <your-repo-url>
cd <your-project-directory>

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required dependencies:
pip install -r requirements.txt

Create and set up the database:

Open the MySQL client and create a new database for the project.
Update the DATABASES section in the settings.py file with your MySQL credentials.

Apply the migrations:
python manage.py migrate

Run the development server:
python manage.py runserver

Access the application:
Open your browser and go to http://127.0.0.1:8000/.
