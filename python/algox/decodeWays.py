def decode_ways(s: str) -> int:
    """
    A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The test cases are generated so that the answer fits in a 32-bit integer.



Example 1:

Input: s = "12"
Output: 2
Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: s = "226"
Output: 3
Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
Example 3:

Input: s = "06"
Output: 0
Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").
Analysis:
    dp[i][j] is the ways to decode for string from index i to j
    """
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][i] = 1
    for i in range(n):
        if s[i] != '0':
            dp[i][i+1] = 1
    for i in range(n):
        for j in range(i+2, n+1):
            cnt = 0
            c = dp[j-1]
            if c != '0':
                cnt = dp[i][j-1]
            tmp = int(s[j-2:j])
            if tmp >= 10 and tmp <= 26:
                cnt += dp[i][j-2]
            dp[i][j] = cnt
    return dp[0][n]


if __name__ == "__main__":
    # s = "12"
    # s = "226"
    s = "06"
    print(decode_ways(s))
