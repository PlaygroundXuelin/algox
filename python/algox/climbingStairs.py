def climbing_stairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
    """
    d_1 = 1
    if n == 1:
        return d_1
    d_2 = 2
    if n == 2:
        return d_2
    for i in range(n-2):
        s = i + 2
        tmp = d_1 + d_2
        d_1 = d_2
        d_2 = tmp
    return d_2


if __name__ == "__main__":
    n = 10
    print(climbing_stairs(n))
