-- a script that lists the number of records with thesame score in the table
SELECT `score`, COUNT(`score`) 'number' FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
