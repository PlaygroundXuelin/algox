def recursive_lcs(x: str, y: str) -> int:
    """
    Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
Analysis:
    iterate over all chars in longer (second) string, 
    maintain an array with value as min index of char in first string.
    the array has property that it keep longest common subseq that ends at that char.

    another example:
    abcdecxc
    acecc
    
    0,1,2,3 
    """
    m = len(x)
    n = len(y)
    if m == 0 or n == 0:
        return 0
    if x[m-1] == y[n-1]:
        return 1 + recursive_lcs(x[:m-1], y[:n-1])
    else:
        return max(recursive_lcs(x[:m-1], y), recursive_lcs(x, y[:n-1]))

    return len(ans)

def dp_lcs(x: str, y:str) -> int:
    m = len(x)
    n = len(y)
    dp = [[0] * (n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    return dp[m][n]


if __name__ == "__main__":
    # x = "aggtab"
    # y = "gxtxayb"
    x = "abc"
    y = "bcdabcd"
    print(dp_lcs(x, y))
