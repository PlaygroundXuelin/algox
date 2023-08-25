def product_arr(nums: [int]) -> [int]:
    """
    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
    Analysis:
    Naive: O(n^2)
    Optimize 1:
    All product, then divide by each: O(n), but use division.
    Optimize 2:
    For each i, maintain products so far:
    pk is the product of all but nums[k]. then p is all nums from 0 to i.
    So for each i, we do product i times. This is O(n^2).
    We need further optimize.
    Using dynamic programming:
    We start from grouping by 1 (n groups).
    pi = 1, gi = ni.
    Then grouping by 2 (n/2 groups):
    For each position in a group, we maintain product without itself, for each group,
    we keep product of all numbers in the group.
    merge group g1 and g2:
    first, the group product will be g1 * g2.
    for each position in the group. pi = pi * gk. gk is the group product of the other group.
    For each group merge, cost is: 1 (all product in group) + items in groups. So total will be nlogn.
    Optimize 3:
    Construct prefix product and suffix product (O(n) for each).
    for each i, Pi = prefix(i-1) * suffix(i+1). O(n).

    :param nums:
    :return:
    """
    n = len(nums)
    prefixes = [1] * (n + 1)
    suffixes = [1] * (n + 1)
    for i in range(n):
        prefixes[i+1] = prefixes[i] * nums[i]
        suffixes[n-i-1] = suffixes[n-i] * nums[n-i-1]
    products = [1] * n
    for i in range(n):
        products[i] = prefixes[i] * suffixes[i+1]
    return products


if __name__ == "__main__":
    nums = [10, 3, 5, 6, 2]
    print(product_arr(nums))
