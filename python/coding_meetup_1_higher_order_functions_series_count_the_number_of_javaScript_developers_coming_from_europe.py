"""
You will be given an array of objects (hashes in ruby) representing data about developers who have signed up to attend
the coding meetup that you are organising for the first time.

Your task is to return the number of JavaScript developers coming from Europe.

For example, given the following list:

lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19,
  'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28,
  'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30,
  'language': 'CSS' }
]
In ruby:

list1 = [
  { first_name: 'Noah', last_name: 'M.', country: 'Switzerland', continent: 'Europe', age: 19, language: 'JavaScript' },
  { first_name: 'Maia', last_name: 'S.', country: 'Tahiti', continent: 'Oceania', age: 28, language: 'JavaScript' },
  { first_name: 'Shufen', last_name: 'L.', country: 'Taiwan', continent: 'Asia', age: 35, language: 'HTML' },
  { first_name: 'Sumayah', last_name: 'M.', country: 'Tajikistan', continent: 'Asia', age: 30, language: 'CSS' }
]
your function should return number 1.

If, there are no JavaScript developers from Europe then your function should return 0.

Notes:

The format of the strings will always be Europe and JavaScript.
All data will always be valid and uniform as in the example above.




This kata is part of the Coding Meetup series which includes a number of short and easy to follow katas which have been
designed to allow mastering the use of higher-order functions. In JavaScript this includes methods like: forEach,
filter, map, reduce, some, every, find, findIndex. Other approaches to solving the katas are of course possible.

Here is the full list of the katas in the Coding Meetup series:

Coding Meetup #1 - Higher-Order Functions Series - Count the number of JavaScript developers coming from Europe

Coding Meetup #2 - Higher-Order Functions Series - Greet developers

Coding Meetup #3 - Higher-Order Functions Series - Is Ruby coming?

Coding Meetup #4 - Higher-Order Functions Series - Find the first Python developer

Coding Meetup #5 - Higher-Order Functions Series - Prepare the count of languages

Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?

Coding Meetup #7 - Higher-Order Functions Series - Find the most senior developer

Coding Meetup #8 - Higher-Order Functions Series - Will all continents be represented?

Coding Meetup #9 - Higher-Order Functions Series - Is the meetup age-diverse?

Coding Meetup #10 - Higher-Order Functions Series - Create usernames

Coding Meetup #11 - Higher-Order Functions Series - Find the average age

Coding Meetup #12 - Higher-Order Functions Series - Find GitHub admins

Coding Meetup #13 - Higher-Order Functions Series - Is the meetup language-diverse?

Coding Meetup #14 - Higher-Order Functions Series - Order the food

Coding Meetup #15 - Higher-Order Functions Series - Find the odd names

Coding Meetup #16 - Higher-Order Functions Series - Ask for missing details
"""


def count_developers(items):
    return len([item for item in items if item.get('language') == 'JavaScript' and item.get('continent') == 'Europe'])
