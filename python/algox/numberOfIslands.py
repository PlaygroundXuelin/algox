def count_islands(a: [[int]]) -> int:
    """
    Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.



Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3


Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

Analysis:
    BFS until connected cells are done, remove the island cells from the map. continue until no more.
    """
    cnt = 0
    m = len(a)
    n = len(a[0])
    x = find_cell(a, m, n)
    while x is not None:
        cnt += 1
        (i, j) = x
        process(a, i, j, m, n)  
        x = find_cell(a, m, n)
    return cnt


def process(a: [[int]], i: int, j: int, m: int, n: int):
    done = set()
    pending = set()
    pending.add((i, j))

    def check(r, c):
        nonlocal pending
        if a[r][c] > 0 and not (r, c) in done:
            pending.add((r, c))
    while len(pending) > 0:
        (i, j) = pending.pop()
        a[i][j] = 0
        if i > 0:
            check(i-1, j)
        if i < m-1:
            check(i+1, j)
        if j > 0:
            check(i, j-1)
        if j < n-1:
            check(i, j+1)
        done.add((i, j))

def find_cell(a: [[int]], m:int, n:int):
    for i in range(m):
        for j in range(n):
            if a[i][j] > 0:
                return (i, j)
    return None


if __name__ == "__main__":
    # grid = [
    #         [1,1,1,1,0],
    #         [1,1,0,1,0],
    #         [1,1,0,0,0],
    #         [0,0,0,0,0]
    #         ]

    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,1]
    ]
    print(count_islands(grid))
