from animales import Leon, Oso, Conejo

comidas = ["carne", "hierba", "pescado"]

print
print("===================================================================")
print("Bienvenidos al mundo animal. Daremos de comer a algunos animales...")
print("===================================================================")
print

leon = Leon("Simba")
leon.hablar()
leon.comer(comidas[1])
leon.comer(comidas[0])

print("===================================================================")

oso = Oso("Yogui")
oso.hablar()
oso.comer(comidas[2])


print("===================================================================")

conejo = Conejo("Tambor")
conejo.hablar()
conejo.comer(comidas[0])

