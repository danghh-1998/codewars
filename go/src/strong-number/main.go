package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
Strong number is the number that the sum of the factorial of its digits is equal to number itself.

For example: 145, since
1! + 4! + 5! = 1 + 24 + 120 = 145
So, 145 is a Strong number.

Task
Given a number, Find if it is Strong or not.
*/

func CalcFactorial(n int) int {
	if n < 2 {
		return 1
	} else {
		return n * CalcFactorial(n-1)
	}
}

func Strong(n int) string {
	numbers := strings.Split(fmt.Sprint(n), "")
	sumFactorial := 0
	for _, val := range numbers {
		number, _ := strconv.Atoi(val)
		sumFactorial += CalcFactorial(number)
	}
	if n == sumFactorial {
		return "STRONG!!!!"
	} else {
		return "Not Strong !!"
	}
}
