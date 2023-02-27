/*
For this challenge you need to create a SELECT statement, this SELECT statement will use an IN to check whether a
department has had a sale with a price over 98.00 dollars.

departments table schema
id
name

sales table schema
id
department_id (department foreign key)
name
price
card_name
card_number
transaction_date

resultant table schema
id
name
NOTE: sometimes a department will not not contain a sale over $98 so just resubmit.
*/

SELECT *
FROM departments
WHERE departments.id IN (SELECT sales.department_id FROM sales WHERE sales.price > 98)