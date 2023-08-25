def longest(nums: [int]) -> dict:
    """
    Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

    Analysis:
    sort would be n log n.
    if for each number,
    maintain longest starting at n and longest stop as n, -1 if no such seq.
    for i, check i-1 and i+1 in the dict

    """
    ls = dict()
    for i in nums:
        if i in ls:
            continue
        a = 1
        b = 1
        right = i+1 in ls
        left = i-1 in ls
        if left and right:
            (_,e1) = ls [i-1]
            b = i-1-e1+1
            (x1, y1) = ls[b]

            (b2, _) = ls[i+1]
            e = i+1+b2-1
            (x2, y2) = ls[e]

            ls[b] = (e-b+1, y1)
            ls[e]=(x2, e-b+1)
        elif left:
            (_,e1) = ls [i-1]
            b = i-1-e1+1
            (x1, y1) = ls[b]
            ls[b] = (i-b+1, y1)
            ls[i] = (1, i-b+1)
        elif right:
            (b2, _) = ls[i+1]
            e = i+1+b2-1
            (x2, y2) = ls[e]
            ls[e] = (x2, e-i+1)
            ls[i] = (e-i+1, 1)
        else:
            ls[i] = (1, 1)
    return ls


if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    # nums = [0,3,7,2,5,8,4,6,0,1]
    d = longest(nums)
    m = 0
    for k in d:
        (a, b) = d[k]
        m = max(m, a, b)
    print(m)



