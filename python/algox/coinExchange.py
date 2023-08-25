def coin_exchange(denoms: [int], n: int) -> [int]:
    """
    You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.



Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0

Analysis:
    dp[i] is the min coins needed for amount i.
    :param denoms:
    :param n:
    :return:
    """

    if n == 0:
        return 0
    dp = [1000000] * (n+1)
    k = len(denoms)
    for i in range(n+1):
        if i == 0:
            dp[i] = 0
            continue
        min_cnt = 1000000
        for j in range(k):
            denom = denoms[j]
            if i < denom:
                break
            min_cnt = min(min_cnt, 1 + dp[i-denom])
        dp[i] = min_cnt
    if dp[n] >= 1000000:
        return -1
    return dp[n]


if __name__ == "__main__":
    denoms = [1, 2, 5]
    total = 11
    print(coin_exchange(denoms, total))
