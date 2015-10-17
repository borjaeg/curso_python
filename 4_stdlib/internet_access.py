import urllib2

for line in urllib2.urlopen('https://docs.python.org/2/tutorial/stdlib.html#operating-system-interface'):
  print line.strip()
