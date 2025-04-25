-- MySQL dump 10.13  Distrib 9.2.0, for Win64 (x86_64)
--
-- Host: localhost    Database: DataGovernance
-- ------------------------------------------------------
-- Server version	9.2.0

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Dumping data for table `dataclassification`
--

LOCK TABLES `dataclassification` WRITE;
/*!40000 ALTER TABLE `dataclassification` DISABLE KEYS */;
INSERT INTO `dataclassification` VALUES (1,'Public Data','Non-sensitive information available for general use'),(2,'Internal Data','Restricted for organizational use only'),(3,'Confidential Data','Includes customer financial details'),(4,'Highly Sensitive Data','Contains personal identification and transaction details');
/*!40000 ALTER TABLE `dataclassification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `datalifecycle`
--

LOCK TABLES `datalifecycle` WRITE;
/*!40000 ALTER TABLE `datalifecycle` DISABLE KEYS */;
INSERT INTO `datalifecycle` VALUES (1,'Creation','Validated input mechanisms are in place'),(2,'Storage','Data must be encrypted and stored securely'),(3,'Access','Strict Role-Based Access Control (RBAC) applies'),(4,'Retention','Transaction records kept for 7 years, customer records for 10 years post-account closure, loan documents for loan duration + 7 years');
/*!40000 ALTER TABLE `datalifecycle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `governancestructure`
--

LOCK TABLES `governancestructure` WRITE;
/*!40000 ALTER TABLE `governancestructure` DISABLE KEYS */;
INSERT INTO `governancestructure` VALUES (1,'Chief Data Officer (CDO)','Oversees data governance strategy and compliance'),(2,'Chief Information Security Officer (CISO)','Ensures data security and risk management'),(3,'Compliance Manager','Ensures adherence to legal and regulatory policies'),(4,'Data Steward','Manages data quality and domain-specific governance');
/*!40000 ALTER TABLE `governancestructure` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-31 10:57:28
