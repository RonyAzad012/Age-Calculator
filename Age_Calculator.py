from datetime import datetime
from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

def calculate_age(birth_date):
    now = datetime.now()
    birth_date = datetime.strptime(birth_date, '%Y-%m-%d')
    
    # Calculate the time difference
    difference = now - birth_date
    
    # Calculate years
    years = difference.days // 365
    
    # Calculate months
    months = (difference.days % 365) // 30
    
    # Calculate remaining days
    days = (difference.days % 365) % 30
    
    # Calculate hours, minutes, and seconds
    hours = now.hour - birth_date.hour
    minutes = now.minute - birth_date.minute
    seconds = now.second - birth_date.second
    
    return {
        'years': years,
        'months': months,
        'days': days,
        'hours': hours,
        'minutes': minutes,
        'seconds': seconds
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def get_age():
    birth_date = request.json['birthDate']
    return jsonify(calculate_age(birth_date))

if __name__ == '__main__':
    app.run(debug=True)
