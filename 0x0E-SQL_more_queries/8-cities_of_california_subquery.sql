-- script to list all cities in california
SELECT id, name -- list all cities
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = "California");
