/*
For this kata we will be using the DVD Rental database.

Your are working for a company that wants to reward its top 10 customers with a free gift. You have been asked to
generate a simple report that returns the top 10 customers by total amount spent ordered from highest to lowest.
Total number of payments has also been requested.

The query should output the following columns:

customer_id [int4]
email [varchar]
payments_count [int]
total_amount [float]
and has the following requirements:
only returns the 10 top customers, ordered by total amount spent from highest to lowest
*/

select payment.customer_id,
       customer.email,
       sum(amount)::float as total_amount,
       count(amount)      as payments_count
from payment,
     customer
where payment.customer_id = customer.customer_id
group by payment.customer_id, customer.email
order by total_amount desc
limit 10
