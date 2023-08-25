def longest_incr_subseq(nums:[int]) -> int:
    """
    Given an integer array nums, return the length of the longest strictly increasing 
subsequence (don't have to be consecutive)
.

Analysis:
    find the dp formula:
    L(i) being the longest subseq ending at index i.
    then double loop in O(n^2)
Optimization:
    binary search:
    """
    n = len(nums)
    l = [1] * n 
    for index in range(n):
        if index == 0:
            continue
        max_len = 1
        for i in range(index):
            if nums[i] >= nums[index]:
                continue
            max_len = max(max_len, l[i] + 1)
        l[index] = max_len
    return max(l)


def n_log_n_longest_incr_subseq(nums:[int]) -> int:
    """ n log n optimization
    The answer maintains a list of increasing subseq,
    and the last element is the smallest of the last element of
    all increasing subseq of the same length.
    """
    ans = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i] > ans[-1]:
            ans.append(nums[i])
        else:
            l = 0
            r = len(ans) - 1
            while l < r:
                m = (l + r) // 2
                if ans[m] < nums[i]:
                    l = m + 1
                else:
                    r = m
            ans[l] = nums[i]
    return len(ans)


if __name__ == "__main__":
    arr = [50, 3, 10, 7, 40, 80]
    # arr = [50, 4, 5, 6, 3, 10, 7, 40, 80]
    # arr = [7,7,7,7,7,7,7]
    print(n_log_n_longest_incr_subseq(arr))

