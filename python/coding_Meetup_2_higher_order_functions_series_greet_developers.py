"""
You will be given an array of objects (associative arrays in PHP) representing data about developers who have signed up
to attend the next coding meetup that you are organising.

Your task is to return an array where each object will have a new property 'greeting' with the following string value:

Hi < firstName here >, what do you like the most about < language here >?

For example, given the following input array:

list1 = [
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
  'language': 'Java' },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35,
  'language': 'Python' },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32,
  'language': 'Ruby' }
]
your function should return the following array:

[
  { 'firstName': 'Sofia', 'lastName': 'I.', 'country': 'Argentina', 'continent': 'Americas', 'age': 35,
  'language': 'Java',
    'greeting': 'Hi Sofia, what do you like the most about Java?'
  },
  { 'firstName': 'Lukas', 'lastName': 'X.', 'country': 'Croatia', 'continent': 'Europe', 'age': 35, 'language':
  'Python',
    'greeting': 'Hi Lukas, what do you like the most about Python?'
  },
  { 'firstName': 'Madison', 'lastName': 'U.', 'country': 'United States', 'continent': 'Americas', 'age': 32, '
  language': 'Ruby',
    'greeting': 'Hi Madison, what do you like the most about Ruby?'
  }
]
Notes:

The order of the properties in the objects does not matter.
The input array will always be valid and formatted as in the example above.

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


def greet_developers(items):
    for item in items:
        item['greeting'] = f'Hi {item.get("firstName")}, what do you like the most about {item.get("language")}?'
    return items
