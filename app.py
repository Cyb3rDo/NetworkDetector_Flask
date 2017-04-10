from flask import Flask, render_template, request
#from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
conn = psycopg2.connect(database="network", user="postgres", password="#######", host="127.0.0.1", port="5432")
cur = conn.cursor()

# @ signifies a decorator - way to wrap a function and modifying its behavior
@app.route("/")
def DetectNetwork():
    return render_template('index.html')

@app.route("/-",methods=['POST'])
def res():
    get=request.form['search']
    search='1-876-'+get
    cur.execute("SELECT prefix, carrier, type from carrier")
    rows = cur.fetchall()
    for row in rows:
    	if row[0] == search:
    		carrier = row[1]
    		type = row[2]
    return render_template('index.html', carrier=carrier, type=type)

# To use int or float <converter:variable_name>

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')
    
if __name__ == "__main__":
    app.run()