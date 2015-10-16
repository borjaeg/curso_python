import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
			     user = 'curso_dlabs',
			     password = 'pass_curso_dlabs',
			     db = 'curso_dlabs',
			     charset = 'utf8')

try:
  with connection.cursor() as cursor:
    sql = "SELECT * FROM escritores"
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
      print row

finally:
  connection.close()
