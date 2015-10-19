-- DROP DATABASE curso_dlabs;
CREATE DATABASE IF NOT EXISTS curso_dlabs
  DEFAULT CHARACTER SET utf8 
  DEFAULT COLLATE utf8_spanish2_ci;

CREATE USER 'curso_dlabs'@'localhost' IDENTIFIED BY 'pass_curso_dlabs';
GRANT ALL PRIVILEGES ON curso_dlabs.* TO 'curso_dlabs'@'localhost';
FLUSH PRIVILEGES; 

