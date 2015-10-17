from animal import Animal

class Carnivoro(Animal):
  
  def comer(self, comida):
    if comida != "carne":
      print "No me gusta"
      self.accion()
    else:
      print "Me como %s" % comida

class Herbivoro(Animal):
  
  def comer(self, comida):
    if comida != "hierba":
      print "No me gusta"
      self.accion()
    else:
      print "Me como %s" % comida

class Omnivoro(Animal):

  def comer(self, comida):
    print "Me como %s" % comida
    self.accion()  
