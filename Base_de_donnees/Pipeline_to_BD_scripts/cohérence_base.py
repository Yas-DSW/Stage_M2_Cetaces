requête utilisée pour verifiée la cohérence de la base de données :


Vérifier les génes qui ne sont pas répertorier dans la table link : 
select gene."ID", gene."Nom" from gene where gene."ID" not in (select "ID gène" from link) ORDER BY "ID";