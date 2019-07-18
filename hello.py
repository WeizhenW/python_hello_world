from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app  = Flask(__name__)

conn = psycopg2.connect("dbname=python_intro user=postgres")
cur = conn.cursor()

number_array = [1,2,3]

@app.route('/')
def get_array():
    print('server hit')
    cur.execute('SELECT * FROM "test"')
    return render_template('index.html', response=number_array)

@app.route('/', methods=['POST'])
def add_number():
    number_array.append(request.form)
    return render_template('index.html', response=number_array)