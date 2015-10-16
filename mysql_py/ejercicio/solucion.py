
def leer_libros_escritores():
  try:
    f = open('libros.txt', 'r')
    libros_escritores = []
    for line in f.readlines():
      libros_escritores.append(line.strip())

    f.close()
    return libros_escritores

  except Exception as e:
    print e.args[0]

import pymysql.cursors

respuesta = leer_libros_escritores()
# Connect to the database
connection = pymysql.connect(host='localhost',
              user = 'curso_dlabs',
              password = 'pass_curso_dlabs',
              db = 'curso_dlabs',
              charset = 'utf8')

query_read = "SELECT id_escritor FROM escritores WHERE nombre LIKE %s"
query_write = "INSERT INTO libros (titulo, id_escritor) VALUES (%s, %s)"

for registro in respuesta:
  nombre = registro.split(',')[0]
  titulo = registro.split(',')[1][1:]
  print nombre
  print titulo
  try:
    with connection.cursor() as cursor:
      cursor.execute(query_read, (nombre))
      id_autor = cursor.fetchone()
      
      with connection.cursor() as cursor_w:
        cursor_w.execute(query_write, (titulo, id_autor))
        connection.commit()

  except Exception as e:
    print e.args[1]
    connection.rollback()

      
      

