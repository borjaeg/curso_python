# -*- coding: utf-8 -*-
import MySQLdb as mdb

try:
	con = mdb.connect('localhost', 'curso_dlabs', 'pass_curso_dlabs', 'curso_dlabs')
	cur = con.cursor()
	cur.execute("DROP TABLE IF EXISTS escritores")
	cur.execute("CREATE TABLE escritores(id INT PRIMARY KEY AUTO_INCREMENT, nombre VARCHAR(25))")
	cur.execute("INSERT INTO escritores(nombre) VALUES ('Franz Kafka')")
	cur.execute("INSERT INTO escritores(nombre) VALUES ('William Shakespeare')")
	cur.execute("INSERT INTO escritores(nombre) VALUES ('Honore de Balzac')")
	cur.execute("INSERT INTO escritores(nombre) VALUES ('Charles Dickens')")
	cur.execute("INSERT INTO escritores(nombre) VALUES ('Miguel de Cervantes')")
	cur.execute("INSERT INTO escritores(nombre) VALUES ('Stendahl')")
	con.commit()

except medb.Error, e:
	if con:
		con.rollback()
		print "Error %d: %s" % (e.args[0], e.args[1])

finally:
	if con:
		con.close()