from nueva_excepcion import MyError


try:
  raise MyError(2*2)
except MyError as e:
  print "Ha ocurrido la excepcion %s" % e.value
