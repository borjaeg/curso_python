# -*- coding: utf-8 -*-
import random

cota_inf = 1
cota_sup = 100
num = random.randint(cota_inf, cota_sup)

while True:
	print "Adina el número entre %d y %d" % (cota_inf, cota_sup)
	guess = input()
	if int(guess) == num:
		print "Correcto"
		break # Sale del bucle infinito
	elif int(guess) < num:
		print "Más alto"
	elif int(guess) > num:
		print "Mas bajo"