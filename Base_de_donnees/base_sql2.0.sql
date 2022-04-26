create type nvx as enum ('Scaffold', 'complet'); 
create type cptm as enum ('trés social','social', 'moyennement social','solitaire');
create type etats as enum ('pseudogéne','fonctionnel');

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
constraint fk_esp foreign key (espece,genre) references organisme(espece,genre)
);


create table experience(
ID SERIAL,
pipeline varchar(200),
paramétres text,
constraint pk_experience primary key (ID)
);

create table gene(
ID SERIAL,
Nom text,
famille varchar(10),
etat etats,
début int,
fin int,
sequence text,
reference int,
constraint pk_gene primary key(ID)
);

create table link(
ID_assemblie varchar(200),
ID_experience int,
ID_gene int,
constraint pk_link primary key ( ID_assemblie, ID_experience, ID_gene),
constraint fk_link_assemblie foreign key (ID_assemblie) references assemblie(identifiant),
constraint fk_link_experience foreign key (ID_experience) references experience(ID),
constraint fk_link_gene foreign key (ID_gene) references gene(ID)
);

/*
Create View Table_des_familles_de_genes_OR AS SELECT assemblie.genre, 
assemblie.espece, 
count(gene.*) as gènes,
(SELECT count(*) as Pseudogenes FROM gene WHERE gene.etat='pseudogéne'), 
(SELECT count(*) as Gene_fonctionnel FROM gene WHERE gene.etat='fonctionnel'),
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
GROUP BY assemblie.espece, assemblie.genre;*/
