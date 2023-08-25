def missing_num(nums: [int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    """
    n = len(nums)
    x = [0] * (n+1)
    for i in range(n+1):
        x[i] = i
    for i in nums:
        x[i] = -1
    for index, i in enumerate(x):
        if i != -1:
            return index


def xor_missing_num(nums: [int]) -> int:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    """
    n = len(nums)
    x = 0
    for i in range(n):
        x = x ^ (i + 1)
    for i in nums:
        x = x ^ i
    return x


if __name__ == "__main__":
    # nums = [1, 0]
    nums = [9,6,4,2,3,5,7,0,1]
    print(xor_missing_num(nums))
