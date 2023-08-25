def search(nums:[int], target: int) -> int:
    """
    There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
    Analysis:
    similar to find min.
    starts with i = 0 and j = n - 1.
    if i is the max or min, and target is begger than max / smaller than min, return -1.
    if target is within the neigbor range, return the index if equals, otherwise -1.
    else,  take middle m = (i + j) // 2. and decide which part the target should be in and continue.

    """
    n = len(nums)
    i = 0
    j = n - 1
    while True:
        if target == nums[i]:
            return i
        if target == nums[j]:
            return j
        if i == j or j == i + 1:
            return -1
        if j == i + 2:
            if target == nums[i+1]:
                return i + 1
            else:
                return -1
        m = (i + j) // 2
        if nums[m] == target:
            return m

        if nums[i+1] > nums[i]:
            if nums[m] > nums[i+1]:
                if target > nums[i] and target < nums[m]:
                    j = m
                else:
                    i = m
            else:
                if target < nums[m] or target > nums[i]:
                    j = m
                else:
                    i = m
        else:
            if nums[m] < nums[i+1]:
                if target > nums[m] and target < nums[i]:
                    i = m
                else:
                    j = m
            else:
                if target > nums[m] or target < nums[i]:
                    j = m
                else:
                    i = m


if __name__ == "__main__":
    # nums = [4,5,6,7,0,1,2]
    # target = 0
    # nums = [4,5,6,7,0,1,2]
    # target = 3
    nums = [1]
    target = 0
    print(search(nums, target))


