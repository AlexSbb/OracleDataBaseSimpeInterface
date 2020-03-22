from flask import Flask
# pip install flask
from flask import render_template
import json
import cx_Oracle
# pip install cx_Oracle
# + Download and install Instant Client  https://www.oracle.com/database/technologies/instant-client/microsoft-windows-32-downloads.html
# Unzip the packages into a single directory such as C:\oracle\instantclient_12_2
# Add this directory to the PATH environment variable.
app = Flask(__name__)

def dataFromOracle(tableName):
    # readv username and password from file
    with open('user.key', 'r') as f:
        user_dict = json.load(f)
        myUserName = user_dict['Username']
        myPassword = user_dict['Password']
        f.close()
   
    # connection to Oracle DB 
    dsnStr = cx_Oracle.makedsn("studidb.gm.fh-koeln.de", "1521", "vlesung")
    con = cx_Oracle.connect(user=myUserName, password=myPassword, dsn=dsnStr) # Use your User Name and Password
    cur = con.cursor()
    cur.execute('SELECT * FROM '+tableName)
    #this operation takes the column names
    col_names = [row[0] for row in cur.description]  
    #this takes all rows from table
    rows = cur.fetchall()
    # Close connection
    cur.close()
    con.close()
    return(col_names,rows)

@app.route('/')
def index():
    tableName = 'Availability' #Change to the name of an existing table from your database
    columns,rows=dataFromOracle(tableName)
    return render_template('index.html', columns=columns, rows=rows, tableName=tableName)
@app.route('/Amazon')
def Amazon():
    viewName = 'Amazon'
    columns,rows=dataFromOracle(viewName)
    return render_template('index.html', columns=columns, rows=rows, tableName=viewName)    

if __name__ == '__main__':
    app.run()