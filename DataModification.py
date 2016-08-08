'''
Created on 13 Jul 2016

@author: Abhijeet
'''
import zipfile
import os
import fnmatch
import csv
import sqlite3

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
    
def createDatabase():
    database = 'C:\\Users\\Abhijeet\\workspace\\WifiDataLogs\\data\\wifidatabase.db'
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute('''CREATE TABLE logs (Campus, Building, RoomNumber, Day, Date, Time, Year, AssociatedCC, AuthenticatedCC)''')
    creader = csv.reader(open('F:\Research Practicum\Data\logs1.csv', 'rt'), delimiter=',', quotechar='|')
    t = (creader,)
    for t in creader:
        cur.executemany("INSERT INTO logs (Campus, Building, RoomNumber, Day, Date, Time, Year, AssociatedCC, AuthenticatedCC) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", (t,))
    con.commit()
    print()
    print("Database created")


if __name__ == '__main__':
    
    zipextract()
    csvextract()
    removeRedundant()
    separateData()
    createDatabase()