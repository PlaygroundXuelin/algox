def two_sum(nums: [int], target: int):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    d = {}
    for i, n in enumerate(nums):
        j = d.get(target-n, None)
        if j is not None:
            return [j, i]
        d[n] = i
    return None

def three_sum(nums: [int], target: int):
    nums.sort()
    for i, ni in enumerate(nums):
        j = i + 1
        k = len(nums) - 1
        while True:
            if  j >= k:
                break
            sum = nums[j] + nums[k]
            if sum > target-ni:
                k = k - 1
            elif sum < target - ni:
                j = j + 1
            else:
                return [i, j, k]
    return None


def sort_index(nums: [int]):
    return sorted(range(len(nums)), key=lambda k: nums[k])


if __name__ == "__main__":
    print(sort_index([1, 9, 3, 7, 5, 11]))