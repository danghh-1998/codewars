/*
For this challenge you need to create a simple SELECT statement. Your task is to calculate the MIN, MEDIAN and MAX
scores of the students from the results table.

*/

CREATE TABLE student
(
    id   INT PRIMARY KEY,
    name VARCHAR NOT NULL
);

CREATE TABLE result
(
    id         INT PRIMARY KEY,
    student_id INT,
    CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES student (id),
    score      INT
);

SELECT MIN(sum_score),
       MAX(sum_score),
       percentile_cont(0.5) within GROUP ( ORDER BY sum_score ) AS median
FROM (SELECT SUM (score) AS sum_score
    FROM RESULT
    GROUP BY student_id) AS student_score
    limit 1