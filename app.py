# create a project environment and activate the environment
# mkdir myproject
# cd myproject
# python3 -m venv venv
# . venv/bin/activate
# install flask
# pip install Flask


# TURN ON DEBUG MODE
# export FLASK_ENV=development
# export FLASK_DEBUG=1

# by default, flask run will run the app.py; otherwise you need to run export FLASK_APP=filename.py

from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

import psycopg2

app  = Flask(__name__)

conn = psycopg2.connect("dbname=python_intro user=wangwz")
cur = conn.cursor()

fruit_list = ['apple', 'orange', 'banana']



@app.route('/<id>', methods=['GET', 'POST'])
def fruit_route(id):
    def add_fruit(fruit):
        fruit_list.append(fruit)
        print(fruit_list)
        return jsonify(fruit_list)

    if request.method == 'GET':
        cur.execute("SELECT * FROM test WHERE id = %s", (id,))
        result = cur.fetchall()
        return render_template('index.html', response=result)
    elif request.method == 'POST':
        print(request.get_json())
        return add_fruit(request.get_json())
