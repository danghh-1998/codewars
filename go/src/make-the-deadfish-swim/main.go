package main

/*
Write a simple parser that will parse and run Deadfish.

Deadfish has 4 commands, each 1 character long:

i increments the value (initially 0)
d decrements the value
s squares the value
o outputs the value into the return array
Invalid characters should be ignored.

Parse("iiisdoso") == []int{8, 64}
*/

func Parse(data string) (result []int) {
	value := 0
	for _, char := range data {
		switch char {
		case 'i':
			value += 1
		case 'd':
			value -= 1
		case 's':
			value *= value
		case 'o':
			result = append(result, value)
		}
	}
	if len(result) == 0 {
		return []int{}
	}
	return
}
