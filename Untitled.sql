CREATE TABLE `clientes` (
  `id_cliente` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(100),
  `email` varchar(100),
  `telefone` varchar(20)
);

CREATE TABLE `produtos` (
  `id_produto` int PRIMARY KEY AUTO_INCREMENT,
  `nome` varchar(100),
  `preco` decimal(10,2),
  `estoque` int
);

CREATE TABLE `pedidos` (
  `id_pedido` int PRIMARY KEY AUTO_INCREMENT,
  `id_cliente` int,
  `data_pedido` date,
  `valor_total` decimal(10,2)
);

CREATE TABLE `itens_pedido` (
  `id_item` int PRIMARY KEY AUTO_INCREMENT,
  `id_pedido` int,
  `id_produto` int,
  `quantidade` int,
  `preco_unitario` decimal(10,2)
);

ALTER TABLE `pedidos` ADD FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`);

ALTER TABLE `itens_pedido` ADD FOREIGN KEY (`id_pedido`) REFERENCES `pedidos` (`id_pedido`);

ALTER TABLE `itens_pedido` ADD FOREIGN KEY (`id_produto`) REFERENCES `produtos` (`id_produto`);
