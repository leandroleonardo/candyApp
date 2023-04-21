DROP DATABASE candyapp;

CREATE DATABASE Candyapp;

USE candyapp;

CREATE TABLE DOCES(
	id_doce int not null primary key auto_increment,
	nome varchar(100),
	ingredientes varchar(1000),
	grupo varchar(100),
	preco float
);

CREATE TABLE CLIENTES(
	id_cliente int not null primary key auto_increment,
	nome varchar(100),
	endereco varchar(1000),
	telefone varchar(25)
);

CREATE TABLE PEDIDOS(

    id_pedido int not null primary key auto_increment,
    id_cliente int,
    id_doce int,

    quantidade varchar(100) not null,
    preco_total float,
    data_entrega date,

    FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente),
    FOREIGN KEY (id_doce) REFERENCES DOCES(id_doce)
);

/* Insert Doces */

INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Pão de mel de chocolate','-','Pão de mel', 6);
INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Pão de mel de doce de leite','-','Pão de mel', 6);
INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Pão de mel de chocolate','-','Pão de mel', 6);
INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Pão de mel de nutella','-','Pão de mel', 6);
INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Cone de nutella','-','Cone trufado', 5);
INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Cone de chocolate','-','Cone trufado', 5);
INSERT INTO Doces(nome, ingredientes, grupo, preco) VALUES ('Cone de doce de leite','-','Cone trufado', 5);

/* Insert usuários */

INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Leandro Leo','-','34658710');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Joao Arnaldo','-','34521324');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Amanda L','-','33563453');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Joao Bertoloti','-','35421327');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Roberto Alves','-','35421327');
INSERT INTO CLIENTES(nome, endereco, telefone) VALUES ('Guilherme Ernesto','-','35421327');

/* Insert Pedidos */

INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (1,2,2,12,'23-04-10');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (1,3,3,18,'23-03-12');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (2,4,1,6,'23-03-13');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (2,4,2,12,'23-04-17');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (3,2,2,12,'23-04-17');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (3,1,4,24,'23-04-17');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (3,6,5,25,'23-04-04');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (4,7,2,10,'23-04-23');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (5,6,2,10,'23-04-23');
INSERT INTO PEDIDOS(id_cliente, id_doce, quantidade, preco_total, data_entrega) VALUES (5,6,3,15,'23-04-04');