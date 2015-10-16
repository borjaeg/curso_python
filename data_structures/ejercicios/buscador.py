import urllib2

indice = {"deportes": ["http://marca.com", "http://as.com", "http://sport.es"],
	  "noticias":["http://elpais.com", "http://elmundo.com", "http://elplural.com", "http://expansion.com"],
	  "programacion": ["http://python.org", "http://java.com"]}

while True:
  busqueda = raw_input("Buscar: ")
  i = 0
  respuestas = indice[busqueda]
  for resultado in respuestas:
    print "%d: %s" % (i, resultado)
    i +=1
  
  exito = raw_input("Acceder a: ")
  print type(respuestas[int(exito)])
  print urllib2.urlopen(str(respuestas[int(exito)])).read()
