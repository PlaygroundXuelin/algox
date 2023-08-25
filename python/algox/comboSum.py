def combo_sum(nums: [int], target: int) -> int:
    """
    Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.



Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
Analysis:
    dp[i] is the combo count for target i.
    dp[0] =  1
    """
    n = len(nums)
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        cnt = 0
        for j in range(n):
            num = nums[j]
            if i < num:
                continue
            cnt += dp[i - num]
        dp[i] = cnt
    return dp[target]


if __name__ == "__main__":
    # nums = [1,2,3]
    # target = 4
    nums = [2,3]
    # 2X5, 3X2 + 2X2,
    target = 10
    # nums = [9]
    # target = 3
    print(combo_sum(nums, target))
