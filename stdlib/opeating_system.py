import os

user = "borja$"

print "Bienvenido a micro-linux"

while True:
  command = raw_input(user + " ")
  if command == "ls" or command == "ls -l":
    for file in os.listdir('.'):
      print file
  elif command == "pwd":
    print os.getcwd()
  elif command == "exit":
    break  
  else:
    print "comando no conocido"
