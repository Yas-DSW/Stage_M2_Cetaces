DROP TYPE IF EXISTS nvx CASCADE;
DROP TYPE IF EXISTS cptm CASCADE;
DROP TYPE IF EXISTS etats CASCADE;

DROP TABLE IF EXISTS gene CASCADE;
DROP TABLE IF EXISTS experience CASCADE;
DROP TABLE IF EXISTS assemblie CASCADE;
DROP TABLE IF EXISTS link CASCADE;
DROP TABLE IF EXISTS organisme CASCADE;

--Creation des types utilisé dans les tables

CREATE TYPE nvx as enum ('Scaffold', 'complet'); 
CREATE TYPE cptm as enum ('trés social','social', 'moyennement social','solitaire');
CREATE TYPE etats as enum ('pseudogéne','fonctionnel');


--Creation des tables et relations

CREATE TABLE organisme (
	espece varchar(100),
	genre varchar(100),
	micro_ordre varchar(100),
	ordre varchar(100),
	habitat varchar(100),
	alimentation varchar(100),
	comportement_social cptm,
	region varchar(150),
	CONSTRAINT 
		pk_organisme PRIMARY KEY (espece,genre)
);


CREATE TABLE assemblie(
	identifiant varchar(200) PRIMARY KEY,
	espece varchar (100),
	genre varchar (100), 
	base_de_donnee varchar(100),
	date_de_publication date,
	niveau_assemblage  nvx,
	score_busco varchar(120),
	CONSTRAINT
		fk_esp FOREIGN KEY (espece,genre) REFERENCES organisme(espece,genre)
);


CREATE TABLE experience(
	ID SERIAL PRIMARY KEY,
	pipeline varchar(200),
	paramétres text
);

CREATE TABLE gene(
	ID SERIAL PRIMARY KEY,
	Nom text,
	Superfamille varchar(100),
	famille varchar(10),
	etat etats,
	début int,
	fin int,
	sequence text,
	reference int
);

CREATE TABLE link(
	ID_assemblie varchar(200),
	ID_experience int,
	ID_gene int,
CONSTRAINT 
	pk_link PRIMARY KEY ( ID_assemblie, ID_experience, ID_gene),
CONSTRAINT
	fk_link_assemblie FOREIGN KEY (ID_assemblie) REFERENCES assemblie(identifiant),
CONSTRAINT 
	fk_link_experience FOREIGN KEY (ID_experience) REFERENCES experience(ID),
CONSTRAINT 
	fk_link_gene FOREIGN KEY (ID_gene) REFERENCES gene(ID)
);


