/*
Do you know recursion?
This is a kata series that you can only solve using recursion.
##1 - Factorial

In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less
than or equal to n. For example,

5! = 5 * 4 * 3 * 2 * 1 = 120.

The value of 0! is 1.

#Your task

You have to create the function factorial that receives n and returns n!. You have to use recursion.
*/

WITH RECURSIVE factorial(n) AS (SELECT CASE
                                           WHEN n < 1 THEN 1
                                           ELSE n * factorial(n - 1)
                                           END
                                FROM factorial)
SELECT *
FROM factorial AS COUNT;

SELECT *
FROM factorial(6);