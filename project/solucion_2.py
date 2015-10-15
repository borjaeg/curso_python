import MySQLdb as mdb
import random
import codecs

def retrieve_riddles():
  query = "SELECT texto, solucion FROM adivinanzas"

  try:
    con = mdb.connect('localhost', 'curso_dlabs', 'pass_curso_dlabs', 'curso_dlabs', charset = "utf8")
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    #for row in rows:
    #   print row
    return rows

  except Exception as e:
    if con: 
      con.rollback()
      print e.args[1]

  finally:
    if con:
      con.close()


riddles = retrieve_riddles()

while True:
  rand = random.randint(0, len(riddles)-1) 
  print codecs.encode(riddles[rand][0], 'utf-8')
  answer = raw_input()
  if answer == riddles[rand][1]:
    print "respuesta correcta"
    break
