import sys

try:
    f = open('mifichero.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "No se puede convertir dato en entero"
except:
    print "Error inesperado:", sys.exc_info()[0]
    raise