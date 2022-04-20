create database GROC;

DROP type nvx CASCADE;
DROP type cptm CASCADE;
DROP type etats CASCADE;

DROP table organisme CASCADE;
DROP table assemblie CASCADE;
DROP table experience CASCADE;
DROP table gene CASCADE;

create type nvx as enum ('Scaffold', 'complet'); 
create type cptm as enum ('trés social','social', 'moyennement social','solitaire');
create type etats as enum ('Pseudogéne','Géne fonctionnel');

create table organisme (
espece varchar(100),
genre varchar(100),
micro_ordre varchar(100),
ordre varchar(100),
habitat varchar(100),
alimentation varchar(100),
comportement_social cptm,
region varchar(150),
constraint pk_organisme primary key (espece,genre)
);


create table assemblie(
identifiant varchar(200),
espece varchar (100),
genre varchar (100), 
base_de_donnee varchar(100),
date_de_publication date,
niveau_assemblage  nvx,
constraint pk_assemblie primary key (identifiant),
constraint fk_esp_gen foreign key (espece, genre) references organisme(espece, genre) 
);


create table experience(
ID SERIAL,
identifiant_assemblie varchar(200),
pipeline varchar(200),
Parametre text,
constraint pk_experience primary key (ID),
constraint fk_IDassembly foreign key (identifiant_assemblie) references assemblie(identifiant)
);

create table gene(
nom text,
famille varchar(10),
etat etats,
identifiant_assemblie varchar(200),
ID_experience int,
constraint pk_gene primary key(nom, identifiant_assemblie, ID_experience),
constraint fk_identifiant foreign key (identifiant_assemblie) references assemblie(identifiant),
constraint fk_ID_exp foreign key (ID_EXPERIENCE) references experience(ID)
);

Create View Table_des_familles_de_genes_OR AS SELECT assemblie.genre, 
assemblie.espece, 
count(gene.*) as gènes,
(SELECT count(*) as Pseudogenes FROM gene WHERE gene.etat='Pseudogéne'), 
(SELECT count(*) as Gene_fonctionnel FROM gene WHERE gene.etat='Géne fonctionnel'),
(SELECT count(gene.*) as OR1 FROM gene WHERE gene.famille='OR1'),
(SELECT count(gene.*) as OR2 FROM gene WHERE gene.famille='OR2'),
(SELECT count(gene.*) as OR3 FROM gene WHERE gene.famille='OR3'),
(SELECT count(gene.*) as OR4 FROM gene WHERE gene.famille='OR4'),
(SELECT count(gene.*) as OR5 FROM gene WHERE gene.famille='OR5'),
(SELECT count(gene.*) as OR6 FROM gene WHERE gene.famille='OR6'),
(SELECT count(gene.*) as OR7 FROM gene WHERE gene.famille='OR7'),
(SELECT count(gene.*) as OR8 FROM gene WHERE gene.famille='OR8'),
(SELECT count(gene.*) as OR9 FROM gene WHERE gene.famille='OR9'),
(SELECT count(gene.*) as OR10 FROM gene WHERE gene.famille='OR10'),
(SELECT count(gene.*) as OR11 FROM gene WHERE gene.famille='OR11'),
(SELECT count(gene.*) as OR12 FROM gene WHERE gene.famille='OR12'),
(SELECT count(gene.*) as OR13 FROM gene WHERE gene.famille='OR13'),
(SELECT count(gene.*) as OR14 FROM gene WHERE gene.famille='OR14'),
(SELECT count(gene.*) as OR51 FROM gene WHERE gene.famille='OR51'),
(SELECT count(gene.*) as OR52 FROM gene WHERE gene.famille='OR52'),
(SELECT count(gene.*) as OR55 FROM gene WHERE gene.famille='OR55'),
(SELECT count(gene.*) as OR56 FROM gene WHERE gene.famille='OR56')
FROM gene,assemblie 
WHERE (gene.identifiant_assemblie=assemblie.identifiant)
GROUP BY assemblie.espece, assemblie.genre;
