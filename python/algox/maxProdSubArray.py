def max_prod_subarr(nums:[int])->int:
    """
    Given an integer array nums, find a subarray
 that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
    Analysis:
    similar to max sum of subarray:
    for each i, keep track of:
    max prod of subarray so far: result_i
    and max postfix products max_i
    and min negative postfix products min_negative_i
    :param nums:
    :return:
    """
    n = len(nums)
    result_i = 0
    end_i = -1
    max_i = 0
    min_neg_i = 0
    for i in range(n):
        if nums[i] == 0:
            max_i = 0
            min_neg_i = 0
        elif nums[i] > 0:
            if max_i == 0:
                max_i = nums[i]
            else:
                max_i = max_i * nums[i]
            if min_neg_i != 0:
                min_neg_i = min_neg_i * nums[i]
        elif nums[i] < 0:
            if min_neg_i == 0:
                max_i = 0
            else:
                max_i = min_neg_i * nums[i]
            if max_i == 0:
                min_neg_i = nums[i]
            else:
                min_neg_i = max_i * nums[i]
        if result_i <= max_i:
            result_i = max_i
            end_i = i
    return result_i


if __name__ == "__main__":
    # nums = [2,3,-2,4]
    nums = [-2,0,-1]
    print(max_prod_subarr(nums))

