-- lists the number of records using GROUP BY 'score' in the table second_table in my MySQL server.
-- records are ordered using DESC.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
