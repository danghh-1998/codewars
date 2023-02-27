/*
For this challenge you need to create a simple HAVING statement, you want to count how many people have the same age
and return the groups with 10 or more people who have that age.

people table schema
id
name
age

return table schema
age
total_people
*/

CREATE TABLE if NOT EXISTS people
(
    id
    INT
    PRIMARY
    KEY,
    NAME
    VARCHAR
    NOT
    NULL,
    age
    INT
    NOT
    NULL
);

SELECT age, COUNT(age) AS total_people
FROM people
GROUP BY age
HAVING COUNT(age) >= 10;