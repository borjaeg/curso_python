from tipos import Carnivoro, Herbivoro, Omnivoro
#from tipos import *

class Leon(Carnivoro):

  def accion(self):
    print "Atacar"

class Conejo(Herbivoro):
  
  def accion(self):
    print "Salir corriendo"

class Oso(Omnivoro):
 
  def accion(self):
    print "Sacar la lengua"
