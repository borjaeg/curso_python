# -*- coding: utf-8 -*-
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
			     user = 'curso_dlabs',
			     password = 'pass_curso_dlabs',
			     db = 'curso_dlabs',
			     charset = 'utf8')

try:
  with connection.cursor() as cursor:
    sql = "UPDATE escritores SET nombre = %s WHERE nombre LIKE %s"
    cursor.execute(sql, ("Mario Vargas Llosa", "%balzac%"))

    print "Número de filas actualizadas: ", cursor.rowcount
    
    connection.commit()

except Exception as e:
  connection.rollback()
  print str(e)

finally:
  connection.close()
