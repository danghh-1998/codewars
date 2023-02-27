package main

/*
Yor task is to write function factorial

https://en.wikipedia.org/wiki/Factorial
*/

func Factorial(n int) int {
	if n == 0 || n == 1 {
		return 1
	} else {
		return n * Factorial(n-1)
	}
}
