DROP TABLE IF EXISTS adivinanzas;
CREATE TABLE adivinanzas(
  id_adivinanza INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  texto TEXT,
  solucion VARCHAR(100)
);
