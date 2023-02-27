package main

/*
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

MoveZeros([]int{1, 2, 0, 1, 0, 1, 0, 3, 0, 1}) // returns []int{ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 }
*/

func MoveZeros(arr []int) []int {
	result := make([]int, 0)
	count := 0
	for _, item := range arr {
		if item != 0 {
			result = append(result, item)
		} else {
			count++
		}
	}

	for i := 0; i < count; i++ {
		result = append(result, 0)
	}

	return result
}
