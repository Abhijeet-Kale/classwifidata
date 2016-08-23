'''
Created on 13 Jul 2016

@author: Abhijeet
'''
import zipfile
import os
import fnmatch
import csv
import sqlite3
import pandas as pd
import numpy as np


def zipextract():
    fh = open('F:\Research Practicum\Data\CSI WiFiLogs.zip', 'rb')
    z = zipfile.ZipFile(fh)
    for name in z.namelist():
        outpath = "F:\Research Practicum\Data\WiFiLogs"
        #print(name)
        z.extract(name, outpath)
    print("First zip file extracted")
    fh.close()


def csvextract():
    rootPath = r"F:\Research Practicum\Data\WiFiLogs"
    pattern = '*.zip'
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            ff = open((os.path.join(root, filename)),'rb')
            zz = zipfile.ZipFile(ff)
            outputPath = "F:\Research Practicum\Data\WiFiLogs\csv"
            zz.extract(os.path.splitext(filename)[0],outputPath)
        ff.close()
    print()
    print("All CSV files are extracted from zip folders")


def removeRedundant():
    rootPathCSV = r"F:\Research Practicum\Data\WiFiLogs\csv"
    patternCSV = '*.CSV'
    FIRST_ROW_NUM = 1
    ROWS_TO_DELETE = []
    #print(ROWS_TO_DELETE)
    for root,dirs,files in os.walk(rootPathCSV):
        for filename in fnmatch.filter(files,patternCSV):
            with open(os.path.join(root, filename), 'r') as inputfile:
                MyData = csv.reader(inputfile)
                index = 1
                for row in MyData:
                    if row[0] == "Key":
                        #print(index)
                        for i in range (1,index+1):
                            ROWS_TO_DELETE.append(i)
                        with open(os.path.join(root, filename), 'rb') as inp, open('F:\Research Practicum\Data\logs.csv','ab') as outp:
                            outp.writelines(row for row_num, row in enumerate(inp, FIRST_ROW_NUM) if row_num not in ROWS_TO_DELETE)
                    else:
                        index += 1
    print()
    print("Logs are extracted in one CSV file")


def separateData():
    with open('F:\Research Practicum\Data\logs.csv','rt') as csvfile, open('F:\Research Practicum\Data\logs1.csv','wt') as outfile:
        reader = csv.reader(csvfile)
        writer = csv.writer(outfile,  lineterminator='\n')
    
        for row in reader:
            content = list(row[1])
            content1 = list(row[0])
            content2 = list(row[2])
            content3 = list(row[3])
            del row[0:4]
            writer.writerow(row+[''.join(content1[:9])]+[''.join(content1[11:27])]+[''.join(content1[29:])]+[''.join(content[:3])]+[''.join(content[4:10]+content[29:])]+[''.join(content[11:19])]+[''.join(content[20:29])]+[''.join(content2)]+[''.join(content3)])
    print()
    print("New Log is created")


def averageData():
    file1= open('F:\Research Practicum\Data\logs.csv','rt')
    reader = csv.reader(file1)
    new_rows_list = []
    for row in reader:
        content = list(row[3])
        content = ''.join(content)
        new_rows_list.append(float(content)/1.27)

    file1.close()
    
    file2 = open('F:\Research Practicum\Data\logs5.csv','wt')
    writer = csv.writer(file2)
    for val in new_rows_list:
        writer.writerow([val])
    file2.close()

    with open('F:\Research Practicum\Data\logs5.csv','rt') as input1, open('F:\Research Practicum\Data\logs6.csv','wt') as output:
        non_blank = (line for line in input1 if line.strip())
        output.writelines(non_blank)

    a = pd.read_csv('F:\Research Practicum\Data\logs.csv')
    b = pd.read_csv('F:\Research Practicum\Data\logs6.csv')
    frames = [a, b]
    merged = pd.concat(frames, axis=1)
    merged.to_csv('F:\Research Practicum\Data\logs7.csv', index=False)   


def createDatabase():
    database = 'C:\\Users\\Abhijeet\\workspace\\WifiDataLogs\\data\\wifidatabase.db'
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute(''' CREATE TABLE logs (Campus, Building, RoomNumber, Day, Date, Time, Year, AssociatedCC, AuthenticatedCC, AverageUsers)''')
    cur.execute('''CREATE TABLE timetable (Classroom, Date, Time1, Time2, Lectures, RegistersUsers)''')
    cur.execute('''CREATE TABLE newlogs (Room, AverageUsers, Date)''')
    
    creader = csv.reader(open('F:\Research Practicum\Data\logs4.csv', 'rt'), delimiter=',', quotechar='|')
    nreader = csv.reader(open('F:\\Research Practicum\\Data\\timetablesheet.csv', 'rt'))
    ctreader = csv.reader(open('F:\\Research Practicum\\Data\\logs14.csv', 'rt'), delimiter=',', quotechar='|')
    
    t = (creader,)
    for t in creader:
        cur.executemany("INSERT INTO logs (Campus, Building, RoomNumber, Day, Date, Time, Year, AssociatedCC, AuthenticatedCC, AverageUsers) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", (t,))

    nt = (nreader,)
    for nt in nreader:
        cur.executemany("INSERT INTO timetable (Classroom, Date, Time1, Time2, Lectures, RegistersUsers) VALUES (?, ?, ?, ?, ?, ?);", (nt,))
    

    ct = (ctreader,)
    for ct in ctreader:
        cur.executemany("INSERT INTO newlogs (Room, AverageUsers, Date) VALUES (?, ?, ?);", (ct,))
    
    con.commit()
    print()
    print("Database created")


def hourly():
    
    FIRST_ROW_NUM = 1
    ROWS_TO_SELECT = []
    with open('F:\\Research Practicum\\Data\\logs7.csv', 'r') as inputfile:
        MyData = csv.reader(inputfile)
        index = 1
        for row in MyData:
            if row[0] == "Belfield > Computer Science > B-002":
                ROWS_TO_SELECT.append(index)
                index += 1
    
    with open('F:\\Research Practicum\\Data\\logs7.csv', 'rb') as inp, open('F:\Research Practicum\Data\logs8.csv','ab') as outp:
        outp.writelines(row for row_num, row in enumerate(inp, FIRST_ROW_NUM) if row_num in ROWS_TO_SELECT)
    
    ROWS_TO_SELECT1 = []
    with open('F:\\Research Practicum\\Data\\logs7.csv', 'r') as inputfile:
        MyData = csv.reader(inputfile)
        index = 1
        for row in MyData:
            if row[0] == "Belfield > Computer Science > B-003":
                ROWS_TO_SELECT1.append(index)
                index += 1
            else:
                index += 1
    
    with open('F:\\Research Practicum\\Data\\logs7.csv', 'rb') as inp, open('F:\Research Practicum\Data\logs9.csv','ab') as outp:
        outp.writelines(row for row_num, row in enumerate(inp, FIRST_ROW_NUM) if row_num in ROWS_TO_SELECT1)
    
    
    ROWS_TO_SELECT2 = []
    with open('F:\\Research Practicum\\Data\\logs7.csv', 'r') as inputfile:
        MyData = csv.reader(inputfile)
        index = 1
        for row in MyData:
            if row[0] == "Belfield > Computer Science > B-004":
                ROWS_TO_SELECT2.append(index)
                index += 1
            else:
                index += 1
    
    with open('F:\\Research Practicum\\Data\\logs7.csv', 'rb') as inp, open('F:\Research Practicum\Data\logs10.csv','ab') as outp:
        outp.writelines(row for row_num, row in enumerate(inp, FIRST_ROW_NUM) if row_num in ROWS_TO_SELECT2)
    
    

def dataframes():
    df1 = pd.read_csv('F:\\Research Practicum\\Data\\logs8.csv')
    df1 = df1.set_index(['Date'])
    df1.index = pd.to_datetime(df1.index, unit='s')
    ticks = df1.ix[:, ['Campus', 'AverageUsers']]
    volumes = ticks.AverageUsers.resample('60min', how='mean')
    volumes.to_csv('F:\\Research Practicum\\Data\\logs11.csv')
    
    df2 = pd.read_csv('F:\\Research Practicum\\Data\\logs9.csv')
    df2 = df2.set_index(['Date'])
    df2.index = pd.to_datetime(df2.index, unit='s')
    ticks = df2.ix[:, ['Campus', 'AverageUsers']]
    volumes = ticks.AverageUsers.resample('60min', how='mean')
    volumes.to_csv('F:\\Research Practicum\\Data\\logs12.csv')

    df3 = pd.read_csv('F:\\Research Practicum\\Data\\logs10.csv')
    df3 = df3.set_index(['Date'])
    df3.index = pd.to_datetime(df3.index, unit='s')
    ticks = df3.ix[:, ['Campus', 'AverageUsers']]
    volumes = ticks.AverageUsers.resample('60min', how='mean')
    volumes.to_csv('F:\\Research Practicum\\Data\\logs13.csv')
    
    df4 = pd.read_csv('F:\\Research Practicum\\Data\\logs11.csv')
    df5 = pd.read_csv('F:\\Research Practicum\\Data\\logs12.csv')
    df6 = pd.read_csv('F:\\Research Practicum\\Data\\logs13.csv')
    frames = [df4, df5, df6]
    merged = pd.concat(frames, axis=0, join='outer', join_axes=None)
    merged.to_csv('F:\Research Practicum\Data\logs14.csv', index=False)
    
    
if __name__ == '__main__':
    
    zipextract()
    csvextract()
    removeRedundant()
    separateData()
    hourly()
    dataframes()
    averageData()
    createDatabase()