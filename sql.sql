CREATE DATABASE sgcta_db;

USE sgcta_db;

CREATE TABLE abastecimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    numero_requisicao VARCHAR(255) NOT NULL,
    nome_motorista VARCHAR(255) NOT NULL,
    modelo_carro VARCHAR(255) NOT NULL,
    placa_carro VARCHAR(255) NOT NULL,
    combustivel ENUM('diesel', 'gasolina') NOT NULL,
    quantidade_abastecida DECIMAL(10,2) NOT NULL,
    valor_total DECIMAL(10,2) NOT NULL,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
