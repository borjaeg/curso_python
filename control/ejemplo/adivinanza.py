# -*- coding: utf-8 -*-
# Adivinanza infinita
enunciado = """\tEn verdes ramas nací,
\ten molino me estrujaron,
\ten un pozo me metí,
\ty del pozo me sacaron
\ta la cocina a freír\n"""

res = ""

print "\n\tAdivina adivinanza"
print "\t=================="
print enunciado
while res != "aceite":
	res = raw_input("Introduce la respuesta: ")

print "Respuesta correcta"