# -*- coding: utf-8 -*-
import MySQLdb as mdb

con = mdb.connect('localhost', 'curso_dlabs', 'pass_curso_dlabs', 'curso_dlabs')

with con:

	cur = con.cursor()
	cur.execute("UPDATE escritores SET nombre = %s WHERE id = %s",
		("Mario Vargas Llosa", int("4")))

	print "Number of rows updated: ", cur.rowcount