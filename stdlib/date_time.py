# -*- coding: utf-8 -*-
from datetime import date

now = date.today()
print "¿A qué día estamos?"
print now

birthday = date(1990,7,3)
print "dias vivito y coleando"
age = now - birthday
print "%d dias" % age.days
