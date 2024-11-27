from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import sqlite3
import json
import datetime
import random
import webbrowser



def write_data(data):
        current_date = datetime.datetime.now().strftime('%d-%m-%Y')

        conn = sqlite3.connect('zalupaData.db')
        cur = conn.cursor()
        r = random.randint(0,22)
        DATA = (r,current_date)


        for i in data: DATA = DATA + tuple({data[i]})

        print(DATA)
        cur.execute("INSERT INTO manager VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", DATA)
        conn.commit()


def read_data():
        h = []
        conn = sqlite3.connect('zalupaData.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM manager WHERE idu = 21;")
        one_result = cur.fetchone()

        for i in one_result[2:]: h.append(i)

        return h


def write_json(data_set = 0):
        data = data_set
        with open('info.json','w') as of:
                json.dump(data,of)



def read_json():
        with open("info.json") as fh:
                dater = json.load(fh)

        return dater

app = Flask(__name__)


@app.route('/')
def index():
        #, pn = d[0], vt=d[1], sr = d[2], cht = d[3], pt = d[4], sb = d[5], vs = d[6]
        return render_template('hello.html')

@app.route('/dev')
def upd_page():
        #, pn = d[0], vt=d[1], sr = d[2], cht = d[3], pt = d[4], sb = d[5], vs = d[6]
        return render_template('upd.html')

@app.route('/data_post', methods=['POST'])
def data_inside_post():

        re = request.json
        write_json(re)

        return "A?"

@app.route('/data_get')
def data_inside_get():
        g = read_json()

        return g



if __name__ == '__main__':
        webbrowser.open('http://127.0.0.1:5000/')
        app.run(debug=True)
