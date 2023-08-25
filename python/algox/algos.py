import unittest

def two_sum_linear(nums, target):
    m = {}
    for index, num in enumerate(nums):
        if num in m:
            return target - num, num
        m[target - num] = index
    return None


def two_sum_double_pointer(nums, target):
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1
    while nums[left] + nums[right] != target:
        if nums[left] + nums[right] > target:
            left = left + 1
        else:
            right = right - 1
        if left == right:
            return None
    return nums[left], nums[right]


# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
# in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
def max_profit(prices):
    min_price = 1000000000
    profit = 0
    for p in prices:
        if min_price >= p:
            min_price = p
            continue
        if p - min_price > profit:
            profit = p - min_price
    return profit


# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
def distinct_num(nums):
    m = {}
    for num in nums:
        if num in m:
            return True
        m[num] = 1
    return False


# Given an integer array nums, return an array answer such that answer[i] is equal to the product
# of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
def product_except_self_naive(nums):
    p = 1
    result = [1] * len(nums)
    for index, num in enumerate(nums):
        result[index] = p
        for index2 in range(0, index):
            result[index2] = result[index2] * num
        p = p * num
    return result


def product_except_self(nums):
    result = [1] * len(nums)
    # calculate prefix products
    p = 1
    for index, num in enumerate(nums):
        result[index] = p
        p = p * num
    # loop from end to muliply by suffix products
    p = 1
    for index in range(len(nums) - 1, 0, -1):
        p = p * nums[index]
        result[index - 1] = result[index - 1] * p
    return result


# Given an integer array nums, find the subarray which has the largest sum and return its sum.
def max_subarray(nums):
    curr_max = 0
    prefix_max = 0
    for num in nums:
        prefix_max = prefix_max + num
        if prefix_max < 0:
            prefix_max = 0
            continue
        if prefix_max > curr_max:
            curr_max = prefix_max
    return curr_max


# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
# and return the product.
def max_product_subarray(nums):
    prefix_pos_product = 0
    prefix_neg_product = 0
    max_product = 0
    for num in nums:
        if num > 0:
            prefix_neg_product = prefix_neg_product * num
            if prefix_pos_product == 0:
                prefix_pos_product = num
            else:
                prefix_pos_product = prefix_pos_product * num
        elif num < 0:
            prefix_pos_product = prefix_neg_product * num
            if prefix_neg_product == 0:
                prefix_neg_product = num
            else:
                prefix_neg_product = prefix_pos_product * num
        else:
            prefix_pos_product = 0
            prefix_neg_product = 0

        if prefix_pos_product > max_product:
            max_product = prefix_pos_product
    return max_product


# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
# the array nums = [0,1,2,4,5,6,7] might become:
#
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array
# [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
#
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
#
# You must write an algorithm that runs in O(log n) time.
def min_in_rotated_sorted_array(nums):
    n = len(nums)
    start = 0
    end = n
    while end - start > 1:
        if nums[start] < nums[end - 1]:
            return nums[start]
        mid = start + (end - start) // 2
        if nums[start] < nums[mid]:
            start = mid + 1
        else:
            end = mid + 1
    return nums[start]


# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
def three_sum(nums, target):
    nums = sorted(nums)
    n = len(nums)
    result = []
    index = 0
    while index < n - 2:
        num = nums[index]
        right = n - 1
        left = index + 1
        while left < right:
            l_r = nums[left] + nums[right]
            if l_r < target - num:
                left = left + 1
            elif l_r > target - num:
                x = nums[right]
                while right > left and nums[right] == x:
                    right = right - 1
            else:
                result.append([nums[index], nums[left], nums[right]])
                x = nums[left]
                while left < right and nums[left] == x:
                    left = left + 1
        x = nums[index]
        while index < n - 2 and nums[index] == x:
            index = index + 1
    return result


# You are given an integer array height of length n. There are n vertical lines drawn such that
# the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container
# contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
def max_water_container_n_square(heights):
    n = len(heights)
    if n == 2:
        return min(heights[0], heights[1])

    result = 0
    for i in range(1, n):
        curr_max = 0
        for j in range(i, n):
            curr_max = max(curr_max, min(heights[j], heights[j - i]))
        result = max(result, curr_max * i)
    return result


# bit op sum
def bit_sum(a, b):
    if b == 0:
        return a
    else:
        return bit_sum(a ^ b, (a & b) << 1)


# Write a function that takes an unsigned integer and returns the number of '1' bits it has
def one_bits(a):
    cnt = 0
    while a != 0:
        cnt = cnt + (a & 1)
        a = a >> 1
    return cnt


# Given an integer n, return an array ans of length n + 1
# such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i
def count_bits(n):
    cnts = [0] * (n + 1)
    cnts[1] = 1
    if n == 0:
        return cnts
    m = 2
    k = 0
    for i in range(2, n+1):
        if k == m:
            m = m + m
            k = 0
        cnts[i] = 1 + cnts[i - m]
        k = k + 1
    return cnts


# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.
def missing_number(nums):
    n = len(nums)
    total = 0
    for i in range(n + 1):
        total = total + i
    for num in nums:
        total = total - num
    return total


# Reverse bits of a given 32 bits unsigned integer.
def reverse_bits(num):
    result = 0
    for i in range(32):
        if num % 2 == 1:
            result = result + 1
        num = num >> 1
        if i < 31:
            result = result << 1
    return result


# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def climb_stairs(n):
    d0 = 1
    d1 = 1
    for i in range(2, n+1):
        d0, d1 = d1, d0 + d1
    return d1


def climb_stairs_memory(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


# number of different ways of changes for amount/denominations
def coin_change_combos(denoms, amount):
    d_n = len(denoms)
    denoms = sorted(denoms)
    dp = [[0] * d_n] * (amount + 1)
    for k in range(0, d_n):
        dp[0][k] = 1
    for i in range(0, amount+1):
        for k in range(0, d_n):
            if i == 0:
                dp[i][k] = 1
                continue
            if k == 0:
                if i % denoms[k] == 0:
                    dp[i][k] = 1
                else:
                    dp[i][k] = 0
                continue
            tmp = 0
            for m in range(0, (i // denoms[k]) + 1):
                new_rest = i - m * denoms[k]
                tmp = tmp + dp[new_rest][k-1]
            dp[i][k] = tmp
    return dp[amount][d_n - 1]


# You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.
#
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of each kind of coin.
def coin_change_min_coins(denoms, amount):
    d_n = len(denoms)
    denoms = sorted(denoms)
    dp = [[0 for _ in range(d_n)] for _ in range(amount + 1)]
    for k in range(0, d_n):
        dp[0][k] = 0
    for i in range(0, amount+1):
        if i == 0:
            continue
        for k in range(0, d_n):
            if k == 0:
                if i % denoms[k] == 0:
                    tmpVal = (i // (denoms[k]))
                    dp[i][k] = tmpVal
                else:
                    dp[i][k] = -1
                continue
            tmp = -1
            for m in range(0, (i // denoms[k]) + 1):
                new_rest = i - m * denoms[k]
                if dp[new_rest][k - 1] < 0:
                    continue
                new_cnt = dp[new_rest][k-1] + m
                if tmp == -1:
                    tmp = new_cnt
                else:
                    tmp = min(tmp, new_cnt)
            dp[i][k] = tmp
    return dp[amount][d_n - 1]


# Given an integer array nums, return the length of the longest strictly increasing subsequence.
#
# A subsequence is a sequence that can be derived from an array by deleting some or no elements
# without changing the order of the remaining elements. For example,
# [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
def longest_increasing_subseq(nums):
    # TODO
    pass


class TestStringMethods(unittest.TestCase):
    def test_two_sum(self):
        nums = [1, -5, 12, 19, 13]
        target = 14
        expected = (-5, 19)
        # print(f"result: {two_sum_linear(nums, target)}, nums: {nums}, target: {target}")
        self.assertEqual(two_sum_linear(nums, target), expected)
        self.assertEqual(two_sum_double_pointer(nums, target), expected)

    def test_max_profit(self):
        prices = [7, 1, 5, 3, 6, 4]
        expected = 5
        self.assertEqual(max_profit(prices), expected)

    def test_distinct_num(self):
        nums = [1, 3, 5, 7, 3]
        expected = True
        self.assertEqual(distinct_num(nums), expected)

    def test_product_except_self(self):
        nums = [1, 2, 3, 5]
        expected = [30, 15, 10, 6]
        self.assertEqual(product_except_self_naive(nums), expected)
        self.assertEqual(product_except_self(nums), expected)

    def test_max_subarray(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        expected = 6
        self.assertEqual(max_subarray(nums), expected)

    def test_max_product_subarray(self):
        nums = [2, 3, -2, 4]
        expected = 6
        self.assertEqual(max_product_subarray(nums), expected)
        nums = [-2, 0, -1]
        expected = 0
        self.assertEqual(max_product_subarray(nums), expected)

    def test_min_in_rotated_sorted_array(self):
        nums = [3, 4, 5, 1, 2]
        expected = 1
        self.assertEqual(min_in_rotated_sorted_array(nums), expected)
        nums = [4, 5, 6, 7, 0, 1, 2]
        expected = 0
        self.assertEqual(min_in_rotated_sorted_array(nums), expected)
        nums = [11, 13, 15, 17]
        expected = 11
        self.assertEqual(min_in_rotated_sorted_array(nums), expected)

    def test_three_sum(self):
        nums = [-1, 0, 1, 2, -1, -4]
        target = 0
        expected = [[-1, -1, 2], [-1, 0, 1]]
        self.assertEqual(three_sum(nums, target), expected)
        nums = [0, 1, 1]
        expected = []
        self.assertEqual(three_sum(nums, target), expected)
        nums = [0, 0, 0]
        expected = [[0, 0, 0]]
        self.assertEqual(three_sum(nums, target), expected)

    def test_max_water_in_container(self):
        heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        expected = 49
        self.assertEqual(max_water_container_n_square(heights), expected)

    def test_bit_sum(self):
        a, b = 1, 2
        expected = 3
        self.assertEqual(bit_sum(a, b), expected)
        a, b = 2, 3
        expected = 5
        self.assertEqual(bit_sum(a, b), expected)

    def test_one_bits(self):
        num = int('00000000000000000000000000001011', 2)
        expected = 3
        self.assertEqual(one_bits(num), expected)

    def test_count_bits(self):
        n = 5
        expected = [0, 1, 1, 2, 1, 2]
        self.assertEqual(count_bits(n), expected)

    def test_missing_num(self):
        nums = [9,6,4,2,3,5,7,0,1]
        expected = 8
        self.assertEqual(missing_number(nums),expected)

    def test_reverse_bits(self):
        num = int('00000010100101000001111010011100', 2)
        expected = int('00111001011110000010100101000000', 2)
        self.assertEqual(reverse_bits(num), expected)

    def test_climb_stairs(self):
        n = 3
        expected = 3
        self.assertEqual(climb_stairs(n), expected)
        self.assertEqual(climb_stairs_memory(n), expected)

    def test_coin_change_combos(self):
        denoms = [1,2,5]
        amount = 11
        expected = 18
        self.assertEqual(coin_change_combos(denoms, amount), expected)

    def test_coin_change_mean_denoms(self):
        denoms = [1,2,5]
        amount = 11
        expected = 3
        self.assertEqual(coin_change_min_coins(denoms, amount), expected)


if __name__ == '__main__':
    unittest.main()
