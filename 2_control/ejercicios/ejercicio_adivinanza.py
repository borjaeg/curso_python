# -*- coding: utf-8 -*-
enunciado = """\tEn verdes ramas nací,
\ten molino me estrujaron,
\ten un pozo me metí,
\ty del pozo me sacaron
\ta la cocina a freír\n"""

res = ""

print "\n\tAdivina adivinanza"
print "\t=================="
print enunciado
intento = 0
while res != "aceite" and intento < 10:
	print "Intento nº %d, te quedan %d" % (intento + 1, 10 - intento)
	res = raw_input("Introduce la respuesta: ")
	intento += 1

if res != "aceite":
	print "Lo siento, número de intentos agotado.\n¿Quieres saber la respuesta?"
	print "1. Sí"
	print "2. No"
	res = raw_input() # ¡¡OJO!!
	if (res == "1" or res == "Sí"):
		print "La respuesta es ACEITE"
	else:
		print "Hasta la próxima"
else:
	print "¡Enhorabuena! La respuesta era aceite :)"		