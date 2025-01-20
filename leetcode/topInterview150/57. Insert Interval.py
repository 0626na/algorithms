"""
leetcode TopInterview 150
57. Insert Interval
Array


You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

 

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
 

Constraints:

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List


def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    merged = []
    inserted = False

    for inter in intervals:
        start, end = inter
        # 추가할 구간보다 앞에 있음
        if newInterval[0] > end:
            merged.append(inter)
        # 추가할 구간보다 뒤에 있음
        elif newInterval[1] < start:
            if not insert:
                merged.append(newInterval)
                inserted = True
            merged.append(inter)
        else:
            newInterval[0] = min(newInterval[0], start)
            newInterval[1] = max(newInterval[1], end)

    if not inserted:
        merged.append(newInterval)

    return merged


insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8])
