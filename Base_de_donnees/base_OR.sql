drop database groc;
create database Groc with TEMPLATE=template0;

DROP type if exists nvx CASCADE;
DROP type if exists cptm CASCADE;
DROP type if exists etats CASCADE;

DROP table if exists organisme CASCADE;
DROP table if exists assemblie CASCADE;
DROP table if exists experience CASCADE;
DROP table if exists gene CASCADE;

create type nvx as enum ('scaffold', 'complet'); 
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
début int,
fin int,
identifiant_assemblie varchar(200),
ID_experience int,
constraint pk_gene primary key(nom, identifiant_assemblie, ID_experience),
constraint fk_identifiant foreign key (identifiant_assemblie) references assemblie(identifiant),
constraint fk_ID_exp foreign key (ID_EXPERIENCE) references experience(ID)
);


