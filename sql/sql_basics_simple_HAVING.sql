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

create table if not exists people (
    id int primary key,
    name varchar not null,
    age int not null
);

select age, count(age) as total_people
from people
group by age
having count(age) >= 10;