import zlib

s = "tres tigres comen trigo en un trigal porque sabe muy muy muy rico"

print("La longitud del texto es  %d") % len(s)
print("Comprimiendo...")
t = zlib.compress(s)
print "La longitud del texto comprimido es  %d" % len(t)

