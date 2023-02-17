-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.10.2-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win64
-- HeidiSQL Versión:             11.3.0.6295
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Volcando estructura de base de datos para junta-de-andalucia
CREATE DATABASE IF NOT EXISTS `junta-de-andalucia` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `junta-de-andalucia`;

-- Volcando estructura para tabla junta-de-andalucia.cliente
CREATE TABLE IF NOT EXISTS `cliente` (
  `RAZON_SOCIAL` varchar(50) DEFAULT NULL,
  `NIF` varchar(50) DEFAULT NULL,
  `CODIGO_DE_INSCRIPCION` varchar(50) DEFAULT NULL,
  `DOMICILIO` varchar(50) DEFAULT NULL,
  `POBLACION` varchar(50) DEFAULT NULL,
  `MUNICIPIO` varchar(50) DEFAULT NULL,
  `PROVINCIA` varchar(50) DEFAULT NULL,
  `PAIS` varchar(50) DEFAULT NULL,
  `CP` varchar(50) DEFAULT NULL,
  `NOMBRE` varchar(50) DEFAULT NULL,
  `APELLIDO` varchar(50) DEFAULT NULL,
  `SEXO` varchar(50) DEFAULT NULL,
  `DNI` varchar(50) DEFAULT NULL,
  `CALIDAD` varchar(50) DEFAULT NULL,
  `CORREO` varchar(50) DEFAULT NULL,
  `TELEFONO` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci COMMENT='Datos del cliente';

-- La exportación de datos fue deseleccionada.

CREATE USER 'junta-de-andalucia'@'localhost' IDENTIFIED BY 'junta-de-andalucia';
GRANT USAGE ON *.* TO 'junta-de-andalucia'@'localhost';
GRANT EXECUTE, SELECT, SHOW VIEW, ALTER, ALTER ROUTINE, CREATE, CREATE ROUTINE, CREATE TEMPORARY TABLES, CREATE VIEW, DELETE, DROP, EVENT, INDEX, INSERT, REFERENCES, TRIGGER, UPDATE, LOCK TABLES  ON `junta-de-andalucia`.* TO 'junta-de-andalucia'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;