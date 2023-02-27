package main

/*
Complete the method which returns the number which is most frequent in the given input array. If there is a tie for
most frequent number, return the largest number among them.

Note: no empty arrays will be given.

Examples
[12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
[12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

*/

func HighestRank(nums []int) int {
	if len(nums) == 0 {
		return -1
	}
	frequentations := make(map[int]int)
	for _, number := range nums {
		if _, exist := frequentations[number]; exist {
			frequentations[number] += 1
		} else {
			frequentations[number] = 1
		}
	}

	result, maxFreq := 0, 0
	for key, freq := range frequentations {
		if freq > maxFreq {
			result = key
			maxFreq = freq
		} else if freq == maxFreq && key > result {
			result = key
		}
	}
	return result
}
