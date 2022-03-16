/*
The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that
character appears only once in the original string, or ")" if that character appears more than once in the original
string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes
Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
the "XXX" is the expected result, not the input!
*/

package kata

import "strings"

func DuplicateEncode(word string) string {
	wordMapper := map[int32]int{}
	word = strings.ToLower(word)
	for _, char := range word {
		if _, found := wordMapper[char]; found {
			wordMapper[char]++
		} else {
			wordMapper[char] = 1
		}
	}

	encoded := ""

	for _, char := range word {
		if wordMapper[char] > 1 {
			encoded += ")"
		} else {
			encoded += "("
		}
	}

	return encoded
}
