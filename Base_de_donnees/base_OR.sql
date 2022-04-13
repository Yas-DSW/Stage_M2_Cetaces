create database GROC;

create type nvx as enum ('Scaffold', 'complet'); 
create type cptm as enum ('trés social','social', 'moyennement social','solitaire');
create type etats as enum ('pseudogene','gene_fonctionnel');

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
famille int,
etat etats,
identifiant_assemblie varchar(200),
ID_experience int,
constraint pk_gene primary key(nom, identifiant_assemblie, ID_experience),
constraint fk_identifiant foreign key (identifiant_assemblie) references assemblie(identifiant),
constraint fk_ID_exp foreign key (ID_assemblie) references experience(ID)
);

Create View Table_des_familles_de_genes_OR AS SELECT assemblie.genre, 
assemblie.espece, 
count(gene.*) as gènes,
(SELECT count(*) as pseudogènes FROM gene WHERE gene.etat='pseudogene'), 
(SELECT count(*) as gènes_fonctionnel FROM gene WHERE gene.etat='gene_fonctionnel'),
(SELECT count(gene.*) as OR1 FROM gene WHERE gene.famille=1),
(SELECT count(gene.*) as OR2 FROM gene WHERE gene.famille=2),
(SELECT count(gene.*) as OR3 FROM gene WHERE gene.famille=3),
(SELECT count(gene.*) as OR4 FROM gene WHERE gene.famille=4),
(SELECT count(gene.*) as OR5 FROM gene WHERE gene.famille=5),
(SELECT count(gene.*) as OR6 FROM gene WHERE gene.famille=6),
(SELECT count(gene.*) as OR7 FROM gene WHERE gene.famille=7),
(SELECT count(gene.*) as OR8 FROM gene WHERE gene.famille=8),
(SELECT count(gene.*) as OR9 FROM gene WHERE gene.famille=9),
(SELECT count(gene.*) as OR10 FROM gene WHERE gene.famille=10),
(SELECT count(gene.*) as OR11 FROM gene WHERE gene.famille=11),
(SELECT count(gene.*) as OR12 FROM gene WHERE gene.famille=12),
(SELECT count(gene.*) as OR13 FROM gene WHERE gene.famille=13),
(SELECT count(gene.*) as OR14 FROM gene WHERE gene.famille=14),
(SELECT count(gene.*) as OR51 FROM gene WHERE gene.famille=51),
(SELECT count(gene.*) as OR52 FROM gene WHERE gene.famille=52),
(SELECT count(gene.*) as OR55 FROM gene WHERE gene.famille=55),
(SELECT count(gene.*) as OR56 FROM gene WHERE gene.famille=56)
FROM gene,assemblie 
WHERE (gene.identifiant_assemblie=assemblie.identifiant)
GROUP BY assemblie.espece, assemblie.genre;
