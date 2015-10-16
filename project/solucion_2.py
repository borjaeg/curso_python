import pymysql.cursors
import random
import codecs

def retrieve_riddles():
  query = "SELECT texto, solucion FROM adivinanzas"
  connection = pymysql.connect(host='localhost',
           user = 'curso_dlabs',
           password = 'pass_curso_dlabs',
           db = 'curso_dlabs',
           charset = 'utf8')
  try:
    with connection.cursor() as cursor:
      cursor = connection.cursor()
      cursor.execute(query)
      rows = cursor.fetchall()
      #for row in rows:
      #   print row
      return rows

  except Exception as e:
    if connection: 
      connection.rollback()
      print e.args[0]

  finally:
    if connection:
      connection.close()


riddles = retrieve_riddles()

while True:
  rand = random.randint(0, len(riddles)-1) 
  print codecs.encode(riddles[rand][0], 'utf-8')
  answer = raw_input()
  if answer == riddles[rand][1]:
    print "respuesta correcta"
    break
