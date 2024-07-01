CREATE TABLE `Dresseurs` (
  `dresseur_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(50) NOT NULL,
  `prenom` VARCHAR(50) NOT NULL,
  `genre` ENUM('Homme','Femme') NOT NULL,
  `est_professeur` ENUM('Oui','Non') NOT NULL DEFAULT 'Non',
  `id_professeur` INT,
  FOREIGN KEY (`id_professeur`) REFERENCES `Dresseurs` (`dresseur_id`)
);

CREATE TABLE `Especes` (
  `espece_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL
);

CREATE TABLE `Monstres` (
  `monstre_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(50) NOT NULL,
  `type` ENUM('Feu','Eau','Plante','Électrique','Glace','Vol','Spectre','Acier','Poison'),
  `point_experience` INT NOT NULL DEFAULT 0,
  `points_de_vie` INT NOT NULL DEFAULT 100,
  `poids` INT NOT NULL DEFAULT 0,
  `taille` INT NOT NULL DEFAULT 0,
  `points_de_puissance` INT NOT NULL DEFAULT 0,
  `niveau` INT NOT NULL DEFAULT 1,
  `espece_id` INT,
  `capturee` ENUM('Oui','Non') NOT NULL DEFAULT 'Non',
  `date_de_capture` TIMESTAMP,
  `dresseur_id` INT,
  FOREIGN KEY (`espece_id`) REFERENCES `Especes` (`espece_id`),
  FOREIGN KEY (`dresseur_id`) REFERENCES `Dresseurs` (`dresseur_id`)
);

CREATE TABLE `Quetes` (
  `quete_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL,
  `localisation` VARCHAR(255),
  `debut` DATE NOT NULL,
  `fin` DATE,
  `point_experience_gagne` INT NOT NULL DEFAULT 0
);

CREATE TABLE `ParticipationQuetes` (
  `participation_quete_id` INT PRIMARY KEY AUTO_INCREMENT,
  `monstre_id` INT,
  `quete_id` INT,
  `date_participation` TIMESTAMP,
  FOREIGN KEY (`monstre_id`) REFERENCES `Monstres` (`monstre_id`),
  FOREIGN KEY (`quete_id`) REFERENCES `Quetes` (`quete_id`)
);

CREATE TABLE `Arenes` (
  `arene_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL,
  `localisation` VARCHAR(255),
  `nombre_de_place` INT NOT NULL DEFAULT 0,
  `taille_m2` INT NOT NULL DEFAULT 0
);

CREATE TABLE `Equipements` (
  `equipement_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL,
  `arene_id` INT,
  `type` ENUM ('Casque', 'Armure', 'Bouclier'),
  FOREIGN KEY (`arene_id`) REFERENCES `Arenes` (`arene_id`)
);

CREATE TABLE `Evenements` (
  `evenement_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL,
  `date_debut` DATE NOT NULL,
  `date_fin` DATE NOT NULL,
  `prix` INT NOT NULL DEFAULT 0,
  `arene_id` INT,
  FOREIGN KEY (`arene_id`) REFERENCES `Arenes` (`arene_id`)
);

CREATE TABLE `ParticipationEvenements` (
  `evenement_id` INT,
  `monstre_id` INT,
  `date_de_participation` DATE NOT NULL,
  PRIMARY KEY (`evenement_id`, `monstre_id`),
  FOREIGN KEY (`evenement_id`) REFERENCES `Evenements` (`evenement_id`),
  FOREIGN KEY (`monstre_id`) REFERENCES `Monstres` (`monstre_id`)
);

CREATE TABLE `Magasins` (
  `magasin_id` INT PRIMARY KEY AUTO_INCREMENT,
  `nom` VARCHAR(100) NOT NULL,
  `localisation` VARCHAR(255)
);

CREATE TABLE `Ventes` (
  `vente_id` INT PRIMARY KEY AUTO_INCREMENT,
  `magasin_id` INT,
  `monstre_id` INT,
  `dresseur_id` INT,
  `prix` INT NOT NULL DEFAULT 0,
  `date_vente` TIMESTAMP,
  FOREIGN KEY (`magasin_id`) REFERENCES `Magasins` (`magasin_id`),
  FOREIGN KEY (`monstre_id`) REFERENCES `Monstres` (`monstre_id`),
  FOREIGN KEY (`dresseur_id`) REFERENCES `Dresseurs` (`dresseur_id`)
);

CREATE TABLE `Combat` (
  `combat_id` INT PRIMARY KEY AUTO_INCREMENT,
  `date_debut` DATE NOT NULL,
  `date_fin` DATE NOT NULL,
  `evenement_id` INT,
  FOREIGN KEY (`evenement_id`) REFERENCES `Evenements` (`evenement_id`)
);

CREATE TABLE `Combat_Monster` (
  `combat_id` INT,
  `monstre_id` INT,
  `gagne` ENUM('Oui','Non') NOT NULL,
  PRIMARY KEY (`combat_id`, `monstre_id`),
  FOREIGN KEY (`combat_id`) REFERENCES `Combat` (`combat_id`),
  FOREIGN KEY (`monstre_id`) REFERENCES `Monstres` (`monstre_id`)
);
