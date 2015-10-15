import os
import MySQLdb as mdb
import codecs

path = 'adivinanzas'

try: 
  con = mdb.connect('localhost', 'curso_dlabs', 'pass_curso_dlabs', 'curso_dlabs')

  for file in os.listdir(path):
    with codecs.open(path + os.path.sep + file, 'r', 'utf-8') as f:
      adivinanza = f.readline().strip()
      solucion = f.readline().strip()
      print adivinanza
      print solucion
      cur = con.cursor()
      cur.execute("INSERT INTO adivinanzas(texto, solucion) VALUES (%s, %s)", (adivinanza, solucion))
      con.commit()

except Exception as e:
  if con:
    con.rollback()
    print "Se ha producido un error"
    print e.args[1]

finally:
  if con:
    con.close()
