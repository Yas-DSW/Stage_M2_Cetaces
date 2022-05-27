SELECT assemblie.genre, 
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


