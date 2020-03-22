Simple Interface to Oracle Database IN Python
=============

# You need
    
    Python.
    Flask.
	cx_Oracle.
	Oracle Instant Client.
	Oracle Database

# Installing Oracle Instant Client

     Download Instant Client from https://www.oracle.com/database/technologies/instant-client/microsoft-windows-32-downloads.html
	 Unzip the packages into a single directory such as C:\oracle\instantclient_19_5
	 Add this directory to the PATH environment variable.

# Install libs
    
    pip install flask
	pip install cx_Oracle

# Settings
	dsnStr = cx_Oracle.makedsn("studidb.gm.fh-koeln.de", "1521", "vlesung") 	# Use addres to your database
    con = cx_Oracle.connect(user=myUserName, password=myPassword, dsn=dsnStr) 	# Use your username and password
	tableName = 'Availability'	# Change to the name of an existing table from your database