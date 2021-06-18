from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/')
def hello():

    with open('wines.csv', mode='r', encoding='utf-8') as csv_file:
        bottles = csv.DictReader(csv_file)
        return render_template('winecellar.html', bottles=bottles)