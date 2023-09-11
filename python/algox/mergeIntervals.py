def merge_intervals(intervals: [tuple[int, int]]) -> [tuple[int, int]]:
    """
    Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.



Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

Analysis:
    1. order by start then end, 
    2. linear to merge adjacent cells
    total: O(nLogn)
feel can not be faster than sort.

    
    """
    intervals = sorted(intervals, key=lambda x: x[0])
    # iterate from beginning, merge all overlappng adjacent ranges, until done
    i = 0
    result = []
    n = len(intervals)
    while i < n:
        start = intervals[i][0]
        end = intervals[i][1]
        j = i+1
        while j<n:
            start1 = intervals[j][0]
            end1 = intervals[j][1]
            if start1 <= end and end1 >= start:
                start = min(start, start1)
                end = max(end, end1)
                j = j + 1
                continue
            i = j-1
            break
        result = result + [[start, end]]
        i = i + 1
    return result


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(intervals))
