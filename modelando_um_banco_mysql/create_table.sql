# Criando a tabela movies
CREATE TABLE movies (
    id          INT PRIMARY KEY AUTO_INCREMENT,
    type        INT NOT NULL,       
    name        VARCHAR (50),
    genre       VARCHAR (20),
    total_ep    INT,
    atual_ep    INT,
    last_view   DATETIME DEFAULT CURRENT_TIMESTAMP
);
