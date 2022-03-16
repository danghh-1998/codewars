package kata

import "strings"
import "math"

/*
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
*/
func FindShort(s string) int {
	words := strings.Split(s, " ")
	minLen := math.MaxInt64
	for _, word := range words {
		wordLen := len(word)
		if len(word) < minLen {
			minLen = wordLen
		}
	}
	return minLen
}
