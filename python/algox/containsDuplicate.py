def contains_duplicate(nums) -> bool:
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
     and return false if every element is distinct.
    Analysis:
    naive: O(n*2)
    Optimize 1: sort and scan. O(n log n)
    Optimize 2: if allows hash. O(n).

    :param nums:
    :return:
    """
