from flask import Flask
from flask import render_template
import csv

app = Flask(__name__)

@app.route('/')
def hello():

    """bottles = [
        {'area': 'Szekszárd', 'producer': 'Pósta', 'name': 'Várdomb Cabernet Franc', 'year':'2017', 'other': "Szűretlen", 'pcs': '4'}, 
        {'area': 'Szekszárd', 'producer': 'Pósta', 'name': 'Cabernet Franc', 'year':'2013', 'other': "", 'pcs': '2'},
        {'area': 'Szekszárd', 'producer': 'Pósta', 'name': 'Cabernet Franc', 'year':'2014', 'other': "", 'pcs': '2'},
        {'area': 'Szekszárd', 'producer': 'Pósta', 'name': 'Merlot', 'year':'2013', 'other': "", 'pcs': '2'},
        {'area': 'Szekszárd', 'producer': 'Pósta', 'name': 'Merlot', 'year':'2015', 'other': "", 'pcs': '2'}
    ]"""

    with open('wines.csv', mode='r', encoding='utf-8') as csv_file:
        bottles = csv.DictReader(csv_file)
        return render_template('winecellar.html', bottles=bottles)