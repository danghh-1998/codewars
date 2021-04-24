package _go

/*
There is an array with some numbers. All numbers are equal except for one. Try to find it!

findUniq([ 1, 1, 1, 2, 1, 1 ]) === 2
findUniq([ 0, 0, 0.55, 0, 0 ]) === 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
*/

func FindUniq(arr[] float32) float32 {
	for idx, _ := range arr {
		switch idx {
		case 0:
			if arr[idx] != arr[idx + 1] && arr[idx] != arr[idx + 2] {
				return arr[idx]
			}
		case len(arr) - 1:
			if arr[idx] != arr[idx - 1] && arr[idx] != arr[idx - 2] {
				return arr[idx]
			}
		default:
			if arr[idx] != arr[idx - 1] && arr[idx] != arr[idx + 1] {
				return arr[idx]
			}
		}
	}
	return 0
}