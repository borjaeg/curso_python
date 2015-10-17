# -*- coding: utf-8 -*-
import pymysql.cursors
import random
import codecs
import sys

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

num_intentos = 10

print 
print "==========================="
print "El Juego de las Adivinanzas"
print "==========================="
print "Introduza 'quit' para salir"
print 

while True:
  rand = random.randint(0, len(riddles)-1) 
  print codecs.encode(riddles[rand][0], 'utf-8')
  for intento in range(num_intentos):
      answer = raw_input()
      if answer == riddles[rand][1]:
        print "Respuesta correcta. A ver si puedes con la siguiente:"
        break
      elif answer == "quit":
        print "Final del juego. ¡Hasta pronto!"
        sys.exit()
      else:
        if intento + 1 < num_intentos:
          print "Respuesta incorrecta. Vuelve a intentarlo, te quedan %d intentos" % (num_intentos - (intento + 1))
        else:
          print "Máximo número de intentos. Probemos con otra adivinanza"
      
