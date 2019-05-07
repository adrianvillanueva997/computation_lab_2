-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: 51.15.59.15    Database: proyecto_computacion
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT = @@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS = @@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION = @@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE = @@TIME_ZONE */;
/*!40103 SET TIME_ZONE = '+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS = @@UNIQUE_CHECKS, UNIQUE_CHECKS = 0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS = @@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS = 0 */;
/*!40101 SET @OLD_SQL_MODE = @@SQL_MODE, SQL_MODE = 'NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES = @@SQL_NOTES, SQL_NOTES = 0 */;

--
-- Table structure for table `Label`
--

DROP TABLE IF EXISTS `Label`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Label`
(
    `id_label`   int(11) NOT NULL AUTO_INCREMENT,
    `label_text` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `ID_Project` int(11)                                 DEFAULT NULL,
    PRIMARY KEY (`id_label`),
    KEY `FK_label_project` (`ID_Project`),
    CONSTRAINT `FK_label_project` FOREIGN KEY (`ID_Project`) REFERENCES `project` (`ID_project`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 29
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `link_web_scrapper`
--

DROP TABLE IF EXISTS `link_web_scrapper`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `link_web_scrapper`
(
    `ID_link`    int(11)                                 NOT NULL AUTO_INCREMENT,
    `url`        varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `ID_project` int(11)                                 NOT NULL,
    `processed`  int(11)                                 NOT NULL DEFAULT '0',
    PRIMARY KEY (`ID_link`),
    KEY `link_web_scrapper_project_FK` (`ID_project`),
    CONSTRAINT `link_web_scrapper_project_FK` FOREIGN KEY (`ID_project`) REFERENCES `project` (`ID_project`)
) ENGINE = InnoDB
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `model`
--

DROP TABLE IF EXISTS `model`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `model`
(
    `ID_model`   int(11)                                 NOT NULL AUTO_INCREMENT,
    `ID_project` int(11)                                 NOT NULL,
    `model_name` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `language`   varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `algorithm`  varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    PRIMARY KEY (`ID_model`),
    KEY `model_project_FK` (`ID_project`),
    CONSTRAINT `model_project_FK` FOREIGN KEY (`ID_project`) REFERENCES `project` (`ID_project`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 88
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project`
--

DROP TABLE IF EXISTS `project`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project`
(
    `ID_project`    int(11)                                 NOT NULL AUTO_INCREMENT,
    `name_project`  varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `ID_invitation` text COLLATE utf8mb4_unicode_ci,
    `Last_Update`   timestamp                               NULL     DEFAULT NULL,
    `Activity`      int(11)                                 NOT NULL DEFAULT '1',
    PRIMARY KEY (`ID_project`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 14
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `project_rel`
--

DROP TABLE IF EXISTS `project_rel`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_rel`
(
    `ID_rel`     int(11) NOT NULL AUTO_INCREMENT,
    `ID_user`    int(11) NOT NULL,
    `ID_project` int(11) NOT NULL,
    PRIMARY KEY (`ID_rel`),
    KEY `project_rel_user_FK` (`ID_user`),
    KEY `project_rel_project_FK` (`ID_project`),
    CONSTRAINT `project_rel_project_FK` FOREIGN KEY (`ID_project`) REFERENCES `project` (`ID_project`),
    CONSTRAINT `project_rel_user_FK` FOREIGN KEY (`ID_user`) REFERENCES `user` (`ID_user`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 15
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `review`
--

DROP TABLE IF EXISTS `review`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `review`
(
    `ID_review`      int(11) NOT NULL AUTO_INCREMENT,
    `ID_project`     int(11) NOT NULL,
    `label`          varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `file_name`      varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
    `text_review`    text COLLATE utf8mb4_unicode_ci,
    `sentiment_pol`  float                                   DEFAULT NULL,
    `sentiment_sub`  float                                   DEFAULT NULL,
    `sentiment_comp` float                                   DEFAULT NULL,
    PRIMARY KEY (`ID_review`),
    KEY `review_project_FK` (`ID_project`),
    CONSTRAINT `review_project_FK` FOREIGN KEY (`ID_project`) REFERENCES `project` (`ID_project`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 1129
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user`
(
    `ID_user`   int(11)                                 NOT NULL AUTO_INCREMENT,
    `user_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `email`     varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `role`      int(11)                                 NOT NULL DEFAULT '0',
    `password`  text COLLATE utf8mb4_unicode_ci         NOT NULL,
    `Actividad` int(11)                                 NOT NULL DEFAULT '1',
    PRIMARY KEY (`ID_user`)
) ENGINE = InnoDB
  AUTO_INCREMENT = 30
  DEFAULT CHARSET = utf8mb4
  COLLATE = utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping routines for database 'proyecto_computacion'
--
/*!40103 SET TIME_ZONE = @OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE = @OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS = @OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS = @OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT = @OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS = @OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION = @OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES = @OLD_SQL_NOTES */;

-- Dump completed on 2019-04-09 21:21:06
