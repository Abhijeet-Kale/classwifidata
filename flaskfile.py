#Importing flask, json and sqlite3
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

#Adding URL rule and generating HTML
@app.route('/', methods=['GET', 'POST'])
def Home():
    return render_template("index.html")


#Function to display all the data as per the room number
@app.route('/json1/<roomno>')
def json2(roomno):
    con = get_db()
    cur=con.cursor()
    cur.execute("select Date, AverageUsers from newlogs where Room=\"{}\"".format(roomno))
    
    data=cur.fetchall()
    print(data)
    return json.dumps(data)


#Function to display data as per the room number, date and between particular time period
@app.route('/datime/<roomno>/<dat>/<time1>/<time2>')
def dateandtime(roomno,dat,time1,time2):
    con = get_db()
    cur = con.cursor()
    cur.execute("select l.Campus, l.Building, l.RoomNumber, l.Day, l.Date, l.Year, Avg(l.AverageUsers), t.RegistersUsers from logs l, timetable t where (l.RoomNumber=t.Classroom and l.Date=t.Date) and l.RoomNumber=\"{}\" and l.Date=\"{}\" and (l.Time between \"{}\" and \"{}\")".format(roomno,dat,time1,time2))
    
    data = cur.fetchall()
    print(data)
    return json.dumps(data)


#Function to display data as per the module
@app.route('/lectureclass/<lecture>')
def lecturetime(lecture):
    con = get_db()
    cur = con.cursor()
    cur.execute("select t.Classroom, t.Lectures, t.Date, l.Time, l.AssociatedCC, l.AuthenticatedCC from logs l, timetable t where (l.RoomNumber=t.Classroom) and t.Lectures=\"{}\" and (l.Time between t.Time1 and t.Time2)".format(lecture))
    
    data = cur.fetchall()
    print(data)
    return json.dumps(data)


#main
if __name__ == "__main__":
    app.run(debug=True)