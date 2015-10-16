import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
							user = 'curso_dlabs',
							password = 'pass_curso_dlabs',
							db = 'curso_dlabs',
							charset = 'utf8')
try:
	with connection.cursor() as cursor:
		cursor.execute("DROP TABLE IF EXISTS escritores")
		cursor.execute("CREATE TABLE escritores(id INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(25))")
		cursor.execute("INSERT INTO escritores(nombre) VALUES ('Franz Kafka')")
		cursor.execute("INSERT INTO escritores(nombre) VALUES ('William Shakespeare')")
		cursor.execute("INSERT INTO escritores(nombre) VALUES ('Honore de Balzac')")
		cursor.execute("INSERT INTO escritores(nombre) VALUES ('Charles Dickens')")
		cursor.execute("INSERT INTO escritores(nombre) VALUES ('Miguel de Cervantes')")
		cursor.execute("INSERT INTO escritores(nombre) VALUES ('Stendahl')")
		connection.commit()

except Exception as e:
	connection.rollback()
	print "Error %s" % e.args[0]

finally:
	connection.close()