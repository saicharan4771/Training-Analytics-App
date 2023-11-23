Training Analytics Application
This repository contains the source code for a small web application that performs analytics on training data. The application is built using Flask, a web framework for Python.

Overview
The application is designed to handle data in a specific JSON format. It provides three main functionalities:

Completed Trainings Count: Lists each completed training along with a count of how many people have completed that training.

Specified Trainings Completed: Given a list of trainings and a fiscal year, it lists all people who completed those trainings in the specified fiscal year.

Expired Trainings: Given a date, finds all people with completed trainings that have already expired or will expire within one month of the specified date. It includes an additional field to indicate whether a training has expired or will expire soon.

Usage
Follow the steps below to run the application:

Clone this repository to your local machine.

bash
Copy code
git clone https://github.com/saicharan4771/Training-Analytics-App.git
Navigate to the project directory.

bash
Copy code
cd Training-Analytics-App
Install the required dependencies.

bash
Copy code
pip install -r requirements.txt
Run the application.

bash
Copy code
python app.py
Open your web browser and go to http://127.0.0.1:5000/ to access the application.

Output Files
The repository includes three output JSON files:

completed_trainings_count.json
specified_trainings_completed.json
expired_trainings.json
These files contain the results of the corresponding functionalities.
