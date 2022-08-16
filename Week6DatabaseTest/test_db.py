import pymysql
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='python_projects',
                            charset='utf8mb4')

with connection.cursor() as cursor:
    sql = "SELECT * FROM sample_table"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
