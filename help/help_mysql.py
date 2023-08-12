from mysql.connector import connect

conn = connect(host='192.168.27.7',
               port=3306,
               user='webuser',
               password='1qaz@WSX',
               database='webdb')


cursor = conn.cursor()
sql = "select * from polls_choice"
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
conn.close()

print(type(results))
print(results)



