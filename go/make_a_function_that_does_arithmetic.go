package _go

/*
Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

The four operators are "add", "subtract", "divide", "multiply".

A few examples:

Arithmetic(5, 2, "add")      => returns 7
Arithmetic(5, 2, "subtract") => returns 3
Arithmetic(5, 2, "multiply") => returns 10
Arithmetic(5, 2, "divide")   => returns 2

*/

func Arithmetic(a int, b int, operator string) int {
	switch operator {
	case "add":
		return a + b
	case "subtract":
		return a - b
	case "multiply":
		return a * b
	case "divide":
		return a / b
	default:
		return 0
	}
}
