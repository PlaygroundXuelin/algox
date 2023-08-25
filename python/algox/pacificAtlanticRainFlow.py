def flow(heights):
    """
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
[0,4]: [0,4] -> Pacific Ocean
       [0,4] -> Atlantic Ocean
[1,3]: [1,3] -> [0,3] -> Pacific Ocean
       [1,3] -> [1,4] -> Atlantic Ocean
[1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
       [1,4] -> Atlantic Ocean
[2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
       [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
[3,0]: [3,0] -> Pacific Ocean
       [3,0] -> [4,0] -> Atlantic Ocean
[3,1]: [3,1] -> [3,0] -> Pacific Ocean
       [3,1] -> [4,1] -> Atlantic Ocean
[4,0]: [4,0] -> Pacific Ocean
       [4,0] -> Atlantic Ocean
Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.
Example 2:

Input: heights = [[1]]
Output: [[0,0]]
Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

 Analysis:
starting from neiboughs to pacific.
ps: cells can flow to pacific
add cells in row 0 and col 0 to memo[1]
for all other cells:
    if one of its neiboughs in ps and height no higher, add it to ps.
    if no new cells added, done, otherwise loop again.

after both ps and as done, intersection of the two sets is the output
    """
    ps = set()
    ts = set()
    m = len(heights)
    n = len(heights[0])
    for i in range(m):
        ps.add((i, 0))
        ts.add((i, n-1))
    for j in range(n):
        ps.add((0, j))
        ts.add((m-1, j))
    process(heights, ps, m, n)
    process(heights, ts, m, n)
    return ps.intersection(ts)


def process(heights, cs, m, n):
    added = False
    for i in range(m):
        for j in range(n):
            if (i, j) in cs:
                continue

            def check(r, c):
                nonlocal cs, added, heights
                if (r, c) in cs and heights[r][c] <= heights[i][j]:
                    cs.add((i, j))
                    added = True
                    return True
                return False
            if i > 0:
                if check(i-1, j):
                    continue
            if i < m-1:
                if check(i+1, j):
                    continue
            if j > 0:
                if check(i, j-1):
                    continue
            if j < n - 1:
                if check(i, j+1):
                    continue

    if added:
        process(heights, cs, m, n)


if __name__ == '__main__':
    # heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    heights = [[1]]
    print(flow(heights))
