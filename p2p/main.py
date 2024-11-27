from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import sqlite3
import json
import datetime
import random
import webbrowser


def write_json(data_set = 0):
        """ 
        Функция для записи в файл JSON
        """
        data = data_set
        with open('info.json','w') as of:
                json.dump(data,of)



def read_json():
        """ 
        Функция для чтения файл JSON
        """
        with open("info.json") as fh:
                dater = json.load(fh)

        return dater

app = Flask(__name__)

@app.route('/') #Главная основная страница
def index():
        
        return render_template('hello.html')

@app.route('/dev') # Шуточная страница, для прикола, это некий DEV-Vlog
def upd_page():
        return render_template('upd.html')

@app.route('/data_post', methods=['POST'])  # страница для общения с JS
def data_inside_post():

        re = request.json
        write_json(re)

        return "A?"

@app.route('/data_get')  # страница для общения с JS
def data_inside_get():
        g = read_json()

        return g



if __name__ == '__main__':
        webbrowser.open('http://127.0.0.1:5000/') # для удобства, чтобы запустить все одним кликом.
        app.run(debug=True)
