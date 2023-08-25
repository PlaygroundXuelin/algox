package gosrc

func MoveZeros(nums []int) {
	if len(nums) <= 1 {
		return
	}
	var nextIndex int
	for i := 0; i < len(nums); i++ {
		if nums[i] == 0 {
			continue
		}
		nums[nextIndex] = nums[i]
		nextIndex++
	}
	for i := nextIndex; i < len(nums); i++ {
		nums[i] = 0
	}
}
