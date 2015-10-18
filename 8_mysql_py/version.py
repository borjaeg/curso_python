import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
			     user = 'curso_dlabs',
			     password = 'pass_curso_dlabs',
			     db = 'curso_dlabs',
			     charset = 'utf8')

try:
  with connection.cursor() as cursor:
    sql = "SELEC VERSION()"
    cursor.execute(sql)
    
    result = cursor.fetchone()
    
    print "Version de la base de datos %s" % result

except Exception as e:
  print "Se ha producido un error"
  print str(e)

finally:
  connection.close()
