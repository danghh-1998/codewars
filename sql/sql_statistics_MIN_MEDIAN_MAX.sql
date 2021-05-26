/*
For this challenge you need to create a simple SELECT statement. Your task is to calculate the MIN, MEDIAN and MAX
scores of the students from the results table.

*/

create table student
(
    id   int primary key,
    name varchar not null
);

create table result
(
    id         int primary key,
    student_id int,
    constraint fk_student_id foreign key (student_id) references student (id),
    score      int
);

select min(sum_score),
       max(sum_score),
       percentile_cont(0.5) within group ( order by sum_score ) as median
from (select sum(score) as sum_score
      from result
      group by student_id) as student_score
limit 1