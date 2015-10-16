CREATE TABLE libros(
  id_libro INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(100),
  id_escritor INT UNSIGNED,
  FOREIGN KEY (id_escritor) REFERENCES escritores(id_escritor)
);


