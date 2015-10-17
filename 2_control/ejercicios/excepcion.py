try:
  print 1/0
except Exception as e:
  print "Se ha producido un error"
  print type(e)
  print e.args

