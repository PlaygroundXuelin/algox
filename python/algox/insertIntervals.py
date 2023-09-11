def insert_interval(intervals: [tuple[int, int]], new_interval: tuple[int, int]):
    """
You are given an array of non-overlapping intervals intervals
where intervals[i] = [starti, endi] represent the start and the end of the
 ith interval and intervals is sorted in ascending order by starti.
 You are also given an interval newInterval = [start, end] that
 represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted
in ascending order by starti and intervals still does not have any overlapping
intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Analysis:
binary search find the range that the start and end of the new interval falls into if overlapped,
or negative index of between two ranges.
Then figure out ranges that needs be merged if any.
Time is O(log N)
space: constant
    """

    if len(intervals) == 0:
        return [new_interval]
    (start, end) = new_interval
    start_index = search(intervals, start)
    end_index = search(intervals, end)
    if start_index < 0:
        from_index = -start_index-1
    else:
        from_index = start_index
    if end_index >= 0:
        to_index = end_index
    else:
        to_index = -end_index-1-1
    need_merge = True
    if start_index < 0 and start_index == end_index:
        need_merge = False
    result = intervals[0:from_index]
    if need_merge:
        new_start = min(start, intervals[from_index][0])
        new_end = max(end, intervals[to_index][1])
        result = result + [(new_start, new_end)]
    else:
        result = result + [(start, end)]
    result = result + intervals[to_index+1:]
    return result


def val_index(intervals: [tuple[int, int]], index: int, start_end: bool) -> int:
    if start_end:
        return intervals[index][0]
    return intervals[index][1]


# search find for val, the overlapped index, negative -index-1 if not overlapped
def search(intervals: [tuple[int, int]], val: int) -> int:
    if val < val_index(intervals, 0, True):
        return -1
    if val > val_index(intervals, len(intervals)-1, False):
        return -len(intervals)-1
    start_index = search_section(intervals, 0, len(intervals)-1, val, True)
    end_index = search_section(intervals, 0, len(intervals)-1, val, False)
    if start_index >= 0:
        return start_index
    if end_index >= 0:
        return end_index
    if end_index == start_index:
        return start_index
    return -end_index-1


def search_section(intervals: [tuple[int, int]], i: int, j: int, val: int, start_end: bool) -> int:
    vi = val_index(intervals, i, start_end)
    vj = val_index(intervals, j, start_end)
    if val < vi:
        return -i-1
    if val > vj:
        return -j-1-1
    if val == vi:
        return i
    if val == vj:
        return j
    m = (i + j) // 2
    vm = val_index(intervals, m, start_end)
    if val == vm:
        return m
    if val < vm:
        if m == 0:
            return -1
        return search_section(intervals, i, m-1, val, start_end)
    if m == len(intervals)-1:
        return -len(intervals)-1
    return search_section(intervals, m+1, j, val, start_end)


if __name__ == "__main__":
    input_intervals = [(1,2),(3,5),(6,7),(8,10),(12,16)]
    input_new_interval = (4, 8)
    print(insert_interval(input_intervals, input_new_interval))
