import sys


def jump_game(nums: [int]) -> int:
    """
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
Analysis:
    memo[i] is the min jumps needed to jump from i to end.
    """
    n = len(nums)
    memo = [-1] * n
    result = jump(nums, 0, n-1, memo)
    if result == sys.maxsize:
        return -1
    return result


def jump(nums: [int], i: int, end: int, memo: [int]) -> int:
    if i == end:
        return 0
    if memo[i] != -1:
        return memo[i]
    if nums[i] == 0:
        memo[i] = sys.maxsize
        return sys.maxsize
    min_jumps = sys.maxsize
    for j in range(nums[i], 0, -1):
        if i + j > end:
            continue
        min_jumps = min(min_jumps, 1+jump(nums, i+j, end, memo))
    memo[i] = min_jumps
    return min_jumps


if __name__ == "__main__":
    ns = [2, 3, 1, 1, 4]
    # ns = [3,2,1,0,4]
    print(jump_game(ns))
