-- phpMyAdmin SQL Dump
-- version 5.0.4deb2
-- https://www.phpmyadmin.net/
--
-- Hôte : localhost:3306
-- Généré le : mar. 03 mai 2022 à 17:33
-- Version du serveur :  10.3.23-MariaDB-1
-- Version de PHP : 7.4.14

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données : `video_surveillance`
--

-- --------------------------------------------------------

--
-- Structure de la table `Alerte`
--

CREATE TABLE `Alerte` (
  `ID_alerte_Alerte` int(10) NOT NULL,
  `type_alerte_Alerte` varchar(30) DEFAULT NULL,
  `date_alerte_Alerte` date DEFAULT NULL,
  `ID_camera_Systeme_Camera` int(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Camera`
--

CREATE TABLE `Camera` (
  `ID_camera_Systeme_Camera` int(11) NOT NULL,
  `Nom_camera_Systeme_Camera` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Camera`
--

INSERT INTO `Camera` (`ID_camera_Systeme_Camera`, `Nom_camera_Systeme_Camera`) VALUES
(1, 'Camera 1'),
(2, 'Camera 2'),
(3, 'Camera 3'),
(4, 'Camera 4');

-- --------------------------------------------------------

--
-- Structure de la table `controle`
--

CREATE TABLE `controle` (
  `ID_camera_Systeme_Camera` int(10) NOT NULL,
  `ID_personnel_Personnel_Technique` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Structure de la table `Personnel_Technique`
--

CREATE TABLE `Personnel_Technique` (
  `ID_personnel_Personnel_Technique` int(100) NOT NULL,
  `User_Name_Utilisateur` varchar(100) DEFAULT NULL,
  `Password_Utilisateur` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Déchargement des données de la table `Personnel_Technique`
--

INSERT INTO `Personnel_Technique` (`ID_personnel_Personnel_Technique`, `User_Name_Utilisateur`, `Password_Utilisateur`) VALUES
(1, 'Armel', '21S2802'),
(2, 'Laure', '21S2812'),
(3, 'Darlin', '21S2810'),
(4, 'Sonia', '18S2120');

--
-- Index pour les tables déchargées
--

--
-- Index pour la table `Alerte`
--
ALTER TABLE `Alerte`
  ADD PRIMARY KEY (`ID_alerte_Alerte`),
  ADD KEY `FK_Alerte_ID_camera_Systeme_Camera` (`ID_camera_Systeme_Camera`);

--
-- Index pour la table `Camera`
--
ALTER TABLE `Camera`
  ADD PRIMARY KEY (`ID_camera_Systeme_Camera`);

--
-- Index pour la table `controle`
--
ALTER TABLE `controle`
  ADD PRIMARY KEY (`ID_camera_Systeme_Camera`,`ID_personnel_Personnel_Technique`),
  ADD KEY `FK_controle_ID_personnel_Personnel_Technique` (`ID_personnel_Personnel_Technique`);

--
-- Index pour la table `Personnel_Technique`
--
ALTER TABLE `Personnel_Technique`
  ADD PRIMARY KEY (`ID_personnel_Personnel_Technique`);

--
-- AUTO_INCREMENT pour les tables déchargées
--

--
-- AUTO_INCREMENT pour la table `Alerte`
--
ALTER TABLE `Alerte`
  MODIFY `ID_alerte_Alerte` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Camera`
--
ALTER TABLE `Camera`
  MODIFY `ID_camera_Systeme_Camera` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT pour la table `controle`
--
ALTER TABLE `controle`
  MODIFY `ID_camera_Systeme_Camera` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT pour la table `Personnel_Technique`
--
ALTER TABLE `Personnel_Technique`
  MODIFY `ID_personnel_Personnel_Technique` int(100) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `Alerte`
--
ALTER TABLE `Alerte`
  ADD CONSTRAINT `FK_Alerte_ID_camera_Systeme_Camera` FOREIGN KEY (`ID_camera_Systeme_Camera`) REFERENCES `Camera` (`ID_camera_Systeme_Camera`);

--
-- Contraintes pour la table `controle`
--
ALTER TABLE `controle`
  ADD CONSTRAINT `FK_controle_ID_camera_Systeme_Camera` FOREIGN KEY (`ID_camera_Systeme_Camera`) REFERENCES `Camera` (`ID_camera_Systeme_Camera`),
  ADD CONSTRAINT `FK_controle_ID_personnel_Personnel_Technique` FOREIGN KEY (`ID_personnel_Personnel_Technique`) REFERENCES `Personnel_Technique` (`ID_personnel_Personnel_Technique`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
