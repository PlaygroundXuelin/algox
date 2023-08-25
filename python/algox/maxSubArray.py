def max_subarray(nums:[int]) -> int:
    """
    Given an integer array nums, find the
subarray
 with the largest sum, and return its sum.
     Analysis:
     Si is max subarray through 0..i
     current max positive postfix sum Pi.
     At i+1:
     max(Pi + nums[i+1} is still positive, Pi+1 = Pi + nums[i+1]
     At end of array at n-1, answer will be max of
       S n-1 and P n-1.
     space: constant
     time: O(n)
    :param nums:
    :return:
    """
    si = 0
    end_i = -1
    pi = 0
    n = len(nums)
    for i in range(n):
        if pi + nums[i] >= 0:
            pi = pi + nums[i]
        else:
            pi = 0
        if end_i == i-1:
            if nums[i] >= 0:
                si = si + nums[i]
                end_i = i
        if si < pi:
            si = pi
            end_i = i
    return si


if __name__ == "__main__":
    # nums = [-2,1,-3,4,-1,2,1,-5,4]
    # nums = [1]
    nums = [5,4,-1,7,8]
    print(max_subarray(nums))