package main

/*
In this example you have to validate if a user input string is alphanumeric. The given string is not
nil/null/NULL/None, so you don't have to check that.

The string has the following conditions to be alphanumeric:

At least one character ("" is not valid)
Allowed characters are uppercase / lowercase latin letters and digits from 0 to 9
No whitespaces / underscore
*/

import "regexp"

func Alphanumeric(str string) bool {
	if len(str) == 0 {
		return false
	}
	pattern, _ := regexp.Compile(`^(\d*\w*)+$`)
	return pattern.MatchString(str)
}
