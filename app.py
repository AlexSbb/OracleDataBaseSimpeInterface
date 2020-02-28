from flask import Flask
from flask import render_template
import json
import cx_Oracle
# + Download and install Instant Client  https://www.oracle.com/database/technologies/instant-client/microsoft-windows-32-downloads.html
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
    con = cx_Oracle.connect(user=myUserName, password=myPassword, dsn=dsnStr)
    cur = con.cursor()

    cur.execute('SELECT * FROM '+tableName)

    #this takes the column names
    col_names = [row[0] for row in cur.description]
    
    #this takes all rows from table
    rows = cur.fetchall()

    cur.close()
    con.close()
    return(col_names,rows)

# test data
# columns = ['STORE_ID', 'STORE_NAME', 'STORE_LINK']
# rows = [(1, 'Actonglobal', 'actonglobal.com'), (2, 'Amazon', 'amazon.com'), (3, 'Arcboardsev', 'arcboardsev.com')]


@app.route('/')
def index():
    columns,rows=dataFromOracle('AVAILABILITY')
    return render_template('index.html', columns=columns, rows=rows)

if __name__ == '__main__':
    app.run()