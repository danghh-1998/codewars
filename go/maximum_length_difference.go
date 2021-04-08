package _go

/*
You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

Find max(abs(length(x) − length(y)))

If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

Example:
a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
mxdiflg(a1, a2) --> 13

Bash note:
input : 2 strings with substrings separated by ,
output: number as a string
*/

func Abs(number int) int {
	if number < 0 {
		return -number
	} else {
		return number
	}

}

func MxDifLg(a1 []string, a2 []string) int {
	if (len(a1) == 0) || (len(a2) == 0) {
		return -1
	}
	maxLen := 0
	for _, str1 := range a1 {
		for _, str2 := range a2 {
			diff := Abs(len(str1)-len(str2))
			if diff > maxLen {
				maxLen = diff
			}
		}
	}
	return maxLen
}
