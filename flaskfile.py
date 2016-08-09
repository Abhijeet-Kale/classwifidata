from flask import Flask, render_template, g
import json
import sqlite3


app = Flask(__name__)
database = 'C:\\Users\\Abhijeet\\workspace\\WifiDataLogs\\data\\wifidatabase.db'

# Connect to database using config.py file
# This contains API key and name of our database file
def db_connect():
    return sqlite3.connect(database)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = db_connect()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/', methods=['GET', 'POST'])
def Home():
    return render_template("index.html")


@app.route('/json1/<roomno>')
def json2(roomno):
    con = get_db()
    cur=con.cursor()
    cur.execute("select * from logs where RoomNumber=\"{}\"".format(roomno))
    
    data=cur.fetchall()
    print(data)
    return json.dumps(data)

@app.route('/day/<roomno>/<weekday>')
def dayWise1(roomno,weekday):
    con = get_db()
    cur=con.cursor()
    cur.execute("select * from logs where RoomNumber=\"{}\" and Day=\"{}\"".format(roomno, weekday))
    
    data=cur.fetchall()
    print(data)
    return json.dumps(data)

@app.route('/date/<roomno>/<date1>')
def dateWise1(roomno,date1):
    con = get_db()
    cur=con.cursor()
    cur.execute("select * from logs where RoomNumber=\"{}\" and Date=\"{}\"".format(roomno,date1))
    
    data=cur.fetchall()
    
    print(data)
    return json.dumps(data)

@app.route('/datime/<roomno>/<dat>/<time1>/<time2>')
def dateandtime(roomno,dat,time1,time2):
    con = get_db()
    cur = con.cursor()
    cur.execute("select * from logs where RoomNumber=\"{}\" and Date=\"{}\" and Time between \"{}\" and \"{}\"".format(roomno,dat,time1,time2))
    
    data = cur.fetchall()
    print(data)
    return json.dumps(data)

@app.route('/lectureclass/<lecture>')
def lecturetime(lecture):
    con = get_db()
    cur = con.cursor()
    cur.execute("select t.Classroom, t.Lectures, t.Date, l.Time, l.AssociatedCC, l.AuthenticatedCC from logs l, timetable t where (l.RoomNumber=t.Classroom) and t.Lectures=\"{}\" and (l.Time between t.Time1 and t.Time2)".format(lecture,lecture))
    
    data = cur.fetchall()
    print(data)
    return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True)