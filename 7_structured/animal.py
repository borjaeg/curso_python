class Animal():
	"""
	Clase que representa a un animal
	"""
	def __init__(self, name):
		self.name = name

	def talk(self):
		print "Sonido cualquiera..."

animal = Animal("cosa")
animal.talk()

class Gato(Animal):
	"""
	Clase que representa a un gato
	"""
	def talk(self):
		print "%s dice Miauu" % (self.name)

cat = Gato("Groucho")
cat.talk()