package main

/*
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging
its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
*/

import (
	"sort"
	"strconv"
	"strings"
)

func NextBigger(number int) int {
	str := strconv.Itoa(number)
	if len(str) < 2 {
		return -1
	}
	pos := len(str) - 2
	flag := false
	for pos >= 0 {
		if str[pos] < str[pos+1] {
			flag = true
			break
		}
		pos--
	}
	if pos == -1 && !flag {
		return -1
	}
	head := str[0:pos]
	tail := str[pos:]
	chars := strings.Split(tail, "")
	sort.Strings(chars)
	tail = strings.Join(chars, "")
	var sign uint8
	for idx, _ := range tail {
		if tail[idx] > str[pos] {
			sign = tail[idx]
			head += string(sign)
			break
		}
	}
	tail = strings.Replace(tail, string(sign), "", 1)
	head += tail
	result, _ := strconv.Atoi(head)
	return result
}
