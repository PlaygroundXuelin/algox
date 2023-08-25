def min_rotated_sorted(nums: [int]) -> int:
    """
    Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
    Analysis:
    look at nums[0]:
        if it's less than both neighbors, it's the answer.
        else: it's bigger than both, min of those if the answer.
        else: find the mid point, and figure out half of the numbers where the min must be in.
    """
    n = len(nums)
    i = 0
    j = n - 1
    while True:
        if i == j:
            return nums[i]
        if j == i + 1:
            return min(nums[i], nums[i+1])
        if j == i + 2:
            return min(nums[i], nums[i+1], nums[i+2])
        if nums[i] < nums[i+1] and nums[i] < nums[j]:
            return nums[i]
        if nums[i] > nums[i+1] and nums[i] > nums[j]:
            return min(nums[i+1], nums[j])
        m = (i + j) // 2
        if nums[i+1] > nums[i]:
            if nums[m] > nums[i+1]:
                i = m
            else:
                j = m
        elif nums[i+1] < nums[i]:
            if nums[m] < nums[i+1]:
                i = m
            else:
                j = m


if __name__ == "__main__":
    # nums=[3,4,5,1,2]
    # nums = [4,5,6,7,0,1,2]
    nums = [11,13,15,17]
    print(min_rotated_sorted(nums))


