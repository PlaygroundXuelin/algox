def rob_houses2(nums: [int]) -> int:
    """
ou are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3
Analysis:
    dp[i, j] is the max with first robbe hourse being the ith and last being the jth.
    """
    if len(nums) == 1:
        return nums[0]
    n = len(nums)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = nums[i]
    for i in range(1, n):
        for j in range(i+2, n):
            if j == n-1 and i == 0:
                dp[i][j] = 0
                continue
            if j-3 >= i:
                dp[i][j] = max(dp[i][j-2] + nums[j], dp[i][j-3] + nums[j])
            else:
                dp[i][j] = max(dp[i][j-2] + nums[j], dp[i][j-3] + nums[j])
    return max(dp[0][n-2], dp[0][n-3], dp[1][n-1], dp[1][n-2],
               dp[2][n-1], dp[2][n-2])
        

if __name__ == "__main__":
    # ns = [2, 3, 2]
    # ns =[1,2,3,1]
    ns = [1,2,3]
    print(rob_houses2(ns))
