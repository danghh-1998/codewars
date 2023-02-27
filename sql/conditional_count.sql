/*
Given a payment table, which is a part of DVD Rental Sample Database, with the following schema

Column       | Type                        | Modifiers
-------------+-----------------------------+----------
payment_id   | integer                     | not null
customer_id  | smallint                    | not null
staff_id     | smallint                    | not null
rental_id    | integer                     | not null
amount       | numeric(5,2)                | not null
payment_date | timestamp without time zone | not null

produce a result set for the report that shows a side-by-side comparison of the number and total amounts of payments
made in Mike's and Jon's stores broken down by months.

The resulting data set should be ordered by month using natural order (Jan, Feb, Mar, etc.).

Note: You don't need to worry about the year component. Months are never repeated because the sample data set contains
payment information only for one year.

The desired output for the report

month | total_count | total_amount | mike_count | mike_amount | jon_count | jon_amount
------+-------------+--------------+------------+-------------+-----------+-----------
2     |             |              |            |             |           |
5     |             |              |            |             |           |
...
month - number of the month (1 - January, 2 - February, etc.)
total_count - total number of payments
total_amount - total payment amount
mike_count - total number of payments accepted by Mike (staff_id = 1)
mike_amount - total amount of payments accepted by Mike (staff_id = 1)
jon_count - total number of payments accepted by Jon (staff_id = 2)
jon_amount - total amount of payments accepted by Jon (staff_id = 2)
*/

SELECT EXTRACT(MONTH FROM payment_date) AS MONTH,
       COUNT(*)                                  AS total_count,
       SUM(amount)                               AS total_amount,
       COUNT(*) filter ( WHERE staff_id = 1 )    AS mike_count,
       SUM(amount) filter ( WHERE staff_id = 1 ) AS mike_amount,
       COUNT(*) filter ( WHERE staff_id = 2 )    AS jon_count,
       SUM(amount) filter ( WHERE staff_id = 2 ) AS jon_amount
FROM payment
GROUP BY MONTH
ORDER BY MONTH;