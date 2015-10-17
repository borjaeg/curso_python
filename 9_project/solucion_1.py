# -*- coding: utf-8 -*-
import os
import pymysql.cursors
import codecs

path = 'adivinanzas'

connection = pymysql.connect(host='localhost',
           user = 'curso_dlabs',
           password = 'pass_curso_dlabs',
           db = 'curso_dlabs',
           charset = 'utf8')

try: 
  with connection.cursor() as cursor:
    for file in os.listdir(path):
      with codecs.open(path + os.path.sep + file, 'r', 'utf-8') as f:
        adivinanza = f.readline().strip()
        solucion = f.readline().strip()
        print adivinanza
        print solucion
        cursor.execute("INSERT INTO adivinanzas(texto, solucion) VALUES (%s, %s)", (adivinanza, solucion))
        connection.commit()

except Exception as e:
  if connection:
    connection.rollback()
    print "Se ha producido un error"
    print e.args[1]

finally:
  if connection:
    connection.close()
