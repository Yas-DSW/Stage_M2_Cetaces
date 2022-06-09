SELECT assemblie."Genre", 
assemblie."Espèce", 
count(gene.*) as "nb gène",
(SELECT count(*) as "nb pseudogènes" FROM gene WHERE gene."Etat"='pseudogène'), 
(SELECT count(*) as "nb gène fonctionnel" FROM gene WHERE gene."Etat"='fonctionnel'),
(SELECT count(gene.*) as "OR1" FROM gene WHERE gene."Famille"='OR1'),
(SELECT count(gene.*) as "OR2" FROM gene WHERE gene."Famille"='OR2'),
(SELECT count(gene.*) as "OR3" FROM gene WHERE gene."Famille"='OR3'),
(SELECT count(gene.*) as "OR4" FROM gene WHERE gene."Famille"='OR4'),
(SELECT count(gene.*) as "OR5" FROM gene WHERE gene."Famille"='OR5'),
(SELECT count(gene.*) as "OR6" FROM gene WHERE gene."Famille"='OR6'),
(SELECT count(gene.*) as "OR7" FROM gene WHERE gene."Famille"='OR7'),
(SELECT count(gene.*) as "OR8" FROM gene WHERE gene."Famille"='OR8'),
(SELECT count(gene.*) as "OR9" FROM gene WHERE gene."Famille"='OR9'),
(SELECT count(gene.*) as "OR10" FROM gene WHERE gene."Famille"='OR10'),
(SELECT count(gene.*) as "OR11" FROM gene WHERE gene."Famille"='OR11'),
(SELECT count(gene.*) as "OR12" FROM gene WHERE gene."Famille"='OR12'),
(SELECT count(gene.*) as "OR13" FROM gene WHERE gene."Famille"='OR13'),
(SELECT count(gene.*) as "OR14" FROM gene WHERE gene."Famille"='OR14'),
(SELECT count(gene.*) as "OR51" FROM gene WHERE gene."Famille"='OR51'),
(SELECT count(gene.*) as "OR52" FROM gene WHERE gene."Famille"='OR52'),
(SELECT count(gene.*) as "OR55" FROM gene WHERE gene."Famille"='OR55'),
(SELECT count(gene.*) as "OR56" FROM gene WHERE gene."Famille"='OR56')
FROM gene,assemblie,link
WHERE gene."ID"=link."ID gène" AND assemblie."ID"=link."ID assemblie"
GROUP BY assemblie."Espèce", assemblie."Genre";


