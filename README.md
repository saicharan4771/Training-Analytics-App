# Training Analytics App

## Overview

The Training Analytics App is a versatile tool that efficiently analyzes training data. It provides a user-friendly interface to:

- **Download JSON:** Easily obtain the generated JSON output for further analysis.
- **Back to Home Feature:** Navigate back to the home page with a single click for a seamless user experience.
- **Versatile Functionality:** Works with any data in the specified format, ensuring adaptability to diverse datasets.
- **Comprehensive Testing:** Clear and effective coverage of all test cases, assuring the application's reliability.


## Features

- **Task 1: Completed Trainings Count**
  - List each completed training with a count of how many people have completed that training.
    <img width="1470" alt="image" src="https://github.com/saicharan4771/Training-Analytics-App/assets/51474996/4825bc0b-8f04-458b-8e77-5bc6ffb3ed68">


- **Task 2: Specified Trainings Completed**
  - Given a list of trainings and a fiscal year, list all people that completed that training in the specified fiscal year.
  - Parameters: Trainings = "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"; Fiscal Year = 2024.
  - <img width="1470" alt="image" src="https://github.com/saicharan4771/Training-Analytics-App/assets/51474996/1446ac53-5c01-4da6-9bfa-dac2ee0d746b">


- **Task 3: Expired Trainings**
  - Given a date, find all people that have any completed trainings that have already expired or will expire within one month of the specified date.
  - Use date: Oct 1st, 2023.
  - <img width="1470" alt="image" src="https://github.com/saicharan4771/Training-Analytics-App/assets/51474996/df4a3afa-e642-4250-b5e3-00e5e60838a6">


## Requirements

- The app should work with any data in the specified format.
- The app should be checked into a publicly accessible GitHub repository.
- The repository should contain the application code and three output JSON files.

## How to Run

1. Clone the repository:**

   ```bash
   git clone https://github.com/saicharan4771/Training-Analytics-App.git
   cd Training-Analytics-App

2. Activate the virtual environment:
   ```bash
      source venv/bin/activate
3. Install dependencies:**
   
   ```bash
      pip3 install -r requirements.txt

4. Run the application:**
   ```bash
      python3 app.py
5. Open your web browser and navigate to http://127.0.0.1:5000/.




6. Output Files
   ```bash
    completed_trainings_count.json
    specified_trainings_completed.json
    expired_trainings.json
