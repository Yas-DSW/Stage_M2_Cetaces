SELECT distinct link.ID_assemblie, link.ID_experience, link.ID_gene, gene.reference
FROM link,gene,assemblie
WHERE link.ID_assemblie IN (SELECT assemblie.identifiant FROM assemblie WHERE espece='bidon1') AND link.ID_gene IN (SELECT gene.ID FROM gene WHERE gene.ID= gene.reference);
