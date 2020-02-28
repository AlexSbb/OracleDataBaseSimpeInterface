import json
import cx_Oracle

with open('user.key', 'r') as f:
    user_dict = json.load(f)
    myUserName = user_dict['Username']
    myPassword = user_dict['Password']
    f.close()

dsnStr = cx_Oracle.makedsn("studidb.gm.fh-koeln.de", "1521", "vlesung")
con = cx_Oracle.connect(user=myUserName, password=myPassword, dsn=dsnStr)

cur = con.cursor()

cur.execute('SELECT * FROM AVAILABILITY')

#this takes the column names
col_names = [row[0] for row in cur.description]
print(col_names)

for result in cur:
    print(result)


# res=[]
# res = cur.fetchall()
# print (res)
# print ('res length = ', len(res))
# if(len(res)>0):
#     print('columnNamber= ', len(res[1]))

cur.close()

print (con.version)
con.close()