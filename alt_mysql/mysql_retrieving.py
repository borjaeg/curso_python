# -*- coding: utf-8 -*-
import MySQLdb as mdb

con = mdb.connect('localhost', 'curso_dlabs', 'pass_curso_dlabs', 'curso_dlabs')

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM escritores")
	rows = cur.fetchall()
	for row in rows:
		print row