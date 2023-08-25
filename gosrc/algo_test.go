package gosrc

import (
	"testing"

	"github.com/stretchr/testify/require"
)

func TestPolinedrome(t *testing.T) {
	type testData struct {
		str      string
		expected int
	}
	for _, td := range []*testData{
		{str: "", expected: 0},
		{str: "a", expected: 1},
		{str: "ab", expected: 1},
		{str: "aa", expected: 2},
		{str: "abc", expected: 1},
		{str: "aac", expected: 2},
		{str: "acc", expected: 2},
		{str: "aaa", expected: 3},
		{str: "abcd", expected: 1},
		{str: "aacd", expected: 2},
		{str: "abbd", expected: 2},
		{str: "abcc", expected: 2},
		{str: "aaad", expected: 3},
		{str: "addd", expected: 3},
		{str: "aaaa", expected: 4},
	} {
		require.Equal(t, td.expected, Polinedrome(td.str), "str: %s", td.str)
	}
}

func TestMoveZeros(t *testing.T) {
	type testData struct {
		nums     []int
		expected []int
	}
	for _, td := range []*testData{
		{nums: nil, expected: nil},
		{nums: []int{}, expected: nil},
		{nums: []int{1}, expected: []int{1}},
		{nums: []int{1, 0}, expected: []int{1, 0}},
		{nums: []int{0, 1}, expected: []int{1, 0}},
		{nums: []int{0, 0, 0}, expected: []int{0, 0, 0}},
		{nums: []int{1, 0, 0}, expected: []int{1, 0, 0}},
		{nums: []int{0, 1, 0}, expected: []int{1, 0, 0}},
		{nums: []int{0, 0, 1}, expected: []int{1, 0, 0}},
		{nums: []int{1, 1, 0}, expected: []int{1, 1, 0}},
		{nums: []int{1, 0, 1}, expected: []int{1, 1, 0}},
		{nums: []int{0, 1, 1}, expected: []int{1, 1, 0}},
		{nums: []int{1, 1, 1}, expected: []int{1, 1, 1}},
	} {
		origLen := len(td.nums)
		origNums := make([]int, origLen)
		copy(origNums, td.nums)
		MoveZeros(td.nums)
		require.Equal(t, origLen, len(td.nums), "origNums: %v", origNums)
		for i := 0; i < origLen; i++ {
			require.Equal(t, td.expected[i], td.nums[i], "origNums: %v", origNums)
		}
	}
}
