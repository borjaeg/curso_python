words = 'Este banco esta ocupado por un padre y un hijo, el padre se llama Juan y el hijo ya te lo he dicho'.split()

result = [[word.upper(), word.lower(), len(word)] for word in words]

for res in result:
  print res
