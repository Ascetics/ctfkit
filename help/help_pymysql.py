import pymysql

conn = pymysql.connect(host='192.168.27.7',
                       port=3306,
                       user='webuser',
                       password='1qaz@WSX',
                       database='webdb')

with conn:
    with conn.cursor() as cursor:
        sql = "select * from polls_choice"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(type(results))
        print(results)

"""
cursor = conn.cursor()
sql = "select * from polls_choice"
cursor.execute(sql)
results = cursor.fetchall()
cursor.close()
conn.close()

print(type(results))
print(results)
"""


