def word_break(s: str, wd: [str]) -> bool:
    """
    Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Analysis:
Naive:
    for each applicable prefix word, check remaining.
    number of words in dictionary: d
    l: string length
    time: d^l
Optimize:
    organize the dictionary as a tree. Then the time component d becomes tree depth.
DP:

   dp[i]: substr 0 to i can be broken into words.
   dp[0] = True
    """
    ss = s
    if len(ss) == 0:
        return True
    for d in wd:
        if ss.startswith(d):
            if word_break(ss[len(d):], wd):
                return True
            continue

    return False


def dp_word_break(s: str, d: [str]) -> str:
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(1, n+1):
        for w in d:
            if i < len(w):
                continue
            if s[i-len(w):i] == w and dp[i-len(w)]:
                dp[i] = True
                break
    return dp[n]


if __name__ == "__main__":
    s = "leetcode"
    d = ["leet", "code"]
    # s = "applepenapple"
    # d = ["apple","pen"]
    # s = "catsandog"
    # d= ["cats","dog","sand","and","cat"]
    print(dp_word_break(s, d))
