# Training Analytics App

## Overview

This application is designed to fulfill the programming exercise for the Application Developer position at the University of Illinois Urbana-Champaign.

## Features

- **Task 1: Completed Trainings Count**
  - List each completed training with a count of how many people have completed that training.

- **Task 2: Specified Trainings Completed**
  - Given a list of trainings and a fiscal year, list all people that completed that training in the specified fiscal year.
  - Parameters: Trainings = "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"; Fiscal Year = 2024.

- **Task 3: Expired Trainings**
  - Given a date, find all people that have any completed trainings that have already expired or will expire within one month of the specified date.
  - Use date: Oct 1st, 2023.

## Requirements

- The app should work with any data in the specified format.
- The app should be checked into a publicly accessible GitHub repository.
- The repository should contain the application code and three output JSON files.

## How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/YOUR_USERNAME/Training-Analytics-App.git
   cd Training-Analytics-App

   Install dependencies:

```bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your web browser and navigate to http://127.0.0.1:5000/.

Output Files
completed_trainings_count.json
specified_trainings_completed.json
expired_trainings.json
