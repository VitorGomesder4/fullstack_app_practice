/*M!999999\- enable the sandbox mode */ 
-- MariaDB dump 10.19-12.2.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: modelodb_academico
-- ------------------------------------------------------
-- Server version	12.2.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*M!100616 SET @OLD_NOTE_VERBOSITY=@@NOTE_VERBOSITY, NOTE_VERBOSITY=0 */;

--
-- Table structure for table `ALUNO`
--

DROP TABLE IF EXISTS `ALUNO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `ALUNO` (
  `CO_ALUNO` int(11) NOT NULL,
  `DT_NASCIMENTO` datetime DEFAULT NULL,
  `SG_SEXO` char(1) DEFAULT NULL,
  `NOME` varchar(20) DEFAULT NULL,
  `CO_ESTADOCIVIL` char(1) DEFAULT NULL,
  `NO_PAI` varchar(70) DEFAULT NULL,
  `NO_MAE` varchar(70) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `ALUNO_TURMA`
--

DROP TABLE IF EXISTS `ALUNO_TURMA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `ALUNO_TURMA` (
  `CO_ALUNO` int(11) NOT NULL,
  `CO_TURMA` char(11) NOT NULL,
  `DT_MATRICULA` datetime DEFAULT NULL,
  `DT_CANCELAMENTO` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `AVALIACAO`
--

DROP TABLE IF EXISTS `AVALIACAO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `AVALIACAO` (
  `CO_ALUNO` int(11) NOT NULL,
  `CO_TURMA` char(11) NOT NULL,
  `CO_DISCIPLINA` char(2) NOT NULL,
  `CO_PROVA` char(3) NOT NULL,
  `DT_AVALIACAO` datetime DEFAULT NULL,
  `NT_AVALIACAO` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `CURSO`
--

DROP TABLE IF EXISTS `CURSO`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `CURSO` (
  `CO_CURSO` int(11) NOT NULL,
  `NOME` char(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `DISCIPLINA`
--

DROP TABLE IF EXISTS `DISCIPLINA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `DISCIPLINA` (
  `CO_DISCIPLINA` char(2) NOT NULL,
  `NO_DISCIPLINA` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `FREQUENCIA`
--

DROP TABLE IF EXISTS `FREQUENCIA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `FREQUENCIA` (
  `CO_ALUNO` int(11) NOT NULL,
  `CO_TURMA` char(11) NOT NULL,
  `CO_DISCIPLINA` char(2) NOT NULL,
  `DT_FREQUENCIA` datetime NOT NULL,
  `FREQUENCIA_` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PROFESSOR`
--

DROP TABLE IF EXISTS `PROFESSOR`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROFESSOR` (
  `CO_PROFESSOR` int(11) NOT NULL,
  `SG_SEXO` char(1) DEFAULT NULL,
  `NOME` varchar(20) DEFAULT NULL,
  `DT_NASCIMENTO` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PROF_TURM_DISC`
--

DROP TABLE IF EXISTS `PROF_TURM_DISC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROF_TURM_DISC` (
  `CO_PROFESSOR` int(11) NOT NULL,
  `CO_TURMA` char(11) NOT NULL,
  `CO_DISCIPLINA` char(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `PROVA`
--

DROP TABLE IF EXISTS `PROVA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `PROVA` (
  `CO_PROVA` char(3) NOT NULL,
  `DS_PROVA` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `TURMA`
--

DROP TABLE IF EXISTS `TURMA`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8mb4 */;
CREATE TABLE `TURMA` (
  `CO_TURMA` char(11) NOT NULL,
  `ANO` char(4) DEFAULT NULL,
  `PERIODO` char(1) DEFAULT NULL,
  `DESCRICAO` char(50) DEFAULT NULL,
  `DT_INICIAL` datetime DEFAULT NULL,
  `DT_FINAL` datetime DEFAULT NULL,
  `NUM_PROVAS` int(11) DEFAULT NULL,
  `CO_CURSO` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*M!100616 SET NOTE_VERBOSITY=@OLD_NOTE_VERBOSITY */;

-- Dump completed on 2026-03-19 23:51:58
