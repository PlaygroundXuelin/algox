def container(heights: [int]) -> (int, int, int):
    """
    You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
    Analysis:
    naive: n^2. check every combo i,j (j > i)
    optimize:
      just need move the shorter height side
    """
    n = len(heights)
    l = 0
    r = n - 1
    m = 0
    ret_l = l
    ret_r = r
    while l < r:
        orig_m = m
        m = max(m, min(heights[l], heights[r]) * (r - l))
        if m > orig_m:
            ret_l = l
            ret_r = r
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return m, ret_l, ret_r


if __name__ == "__main__":
    heights = [1,8,6,2,5,4,8,3,7]
    print(container(heights))
