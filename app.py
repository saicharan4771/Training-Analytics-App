from flask import Flask, render_template, request, send_file
import json
from datetime import datetime, timedelta

app = Flask(__name__)

def read_json(file):
    data = json.load(file)
    return data

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def get_expired_trainings(data, specified_date):
    expired_trainings = []

    for person in data:
        person_entry = {'name': person['name'], 'completions': []}

        for completion in person['completions']:
            if completion['expires'] is not None:
                expire_date = datetime.strptime(completion['expires'], "%m/%d/%Y") + timedelta(days=1)
                days_until_expire = (expire_date - specified_date).days

                if days_until_expire < 0:
                    status = 'expired'
                elif 0 <= days_until_expire <= 30:
                    status = 'expires_soon'
                else:
                    continue  

                person_entry['completions'].append({
                    'name': completion['name'],
                    'status': status
                })

        if person_entry['completions']:
            expired_trainings.append(person_entry)

    return expired_trainings



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/completed_trainings_count', methods=['POST'])
def get_completed_trainings_count():
    file = request.files['file']
    if not file:
        return render_template('output.html', function_name="Completed Trainings Count", output_data={"error": "Please upload a JSON file."})
    
    data = read_json(file)
    completed_trainings_count = {}
    for person in data:
        for completion in person['completions']:
            training_name = completion['name']
            completed_trainings_count[training_name] = completed_trainings_count.get(training_name, 0) + 1
    
    output_file_path = 'completed_trainings_count.json'
    write_json(completed_trainings_count, output_file_path)
    
    return render_template('output.html', function_name="Completed Trainings Count", output_data=completed_trainings_count)

@app.route('/specified_trainings_completed', methods=['POST'])
def get_specified_trainings_completed():
    file = request.files['file']
    if not file:
        return render_template('output.html', function_name="Specified Trainings Completed", output_data={"error": "Please upload a JSON file."})
    
    data = read_json(file)
    
    specified_trainings = [t.strip() for t in request.form.get('trainings').split(',')] 
    fiscal_year = int(request.form.get('fiscal_year'))
    fiscal_year_start = datetime(fiscal_year - 1, 7, 1)
    fiscal_year_end = datetime(fiscal_year, 6, 30)
    
    specified_trainings_completed = {}
    
    for person in data:
        for completion in person['completions']:
            if completion['name'].strip() in specified_trainings:  
                timestamp = datetime.strptime(completion['timestamp'], "%m/%d/%Y")
                if fiscal_year_start <= timestamp <= fiscal_year_end:
                    specified_trainings_completed.setdefault(completion['name'], []).append({
                        'name': person['name'],
                        'timestamp': timestamp.strftime("%m/%d/%Y")
                    })
    
    output_file_path = 'specified_trainings_completed.json'
    write_json(specified_trainings_completed, output_file_path)
    
    return render_template('output.html', function_name="Specified Trainings Completed", output_data=specified_trainings_completed)

@app.route('/expired_trainings', methods=['POST'])
def get_expired_trainings_route():
    file = request.files['file']
    if not file:
        return render_template('output.html', function_name="Expired Trainings", output_data={"error": "Please upload a JSON file."})
    
    data = read_json(file)
    
    expiration_date = datetime.strptime(request.form.get('expiration_date'), "%Y-%m-%d")
    expired_trainings = get_expired_trainings(data, expiration_date)
    
    output_file_path = 'expired_trainings.json'
    write_json(expired_trainings, output_file_path)
    
    return render_template('output.html', function_name="Expired Trainings", output_data=expired_trainings)

@app.route('/download/<function_name>')
def download(function_name):
    file_path = f"{function_name.lower().replace(' ', '_')}.json"
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
