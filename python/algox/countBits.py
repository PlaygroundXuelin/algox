def count_bits(n: int) -> [int]:
    """
    Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
    """
    ans = [0] * (n+1)
    for i in range(n):
        cnt = ans[i]
        k = i
        while k != 0:
            if k & 1 == 1:
                cnt -= 1
                k = k >> 1
            else:
                break
        ans[i+1] = cnt + 1
    return ans

if __name__ == "__main__":
    print(count_bits(5))
