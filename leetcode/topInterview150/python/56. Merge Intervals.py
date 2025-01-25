"""
leetcode Topinterview 150 
56. Merge Intervals
Array, Sorting

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
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort()
    result = []
    merged = []

    for inter in intervals:
        if not merged:
            merged.append(inter[0])
            merged.append(inter[1])
            continue
        a, b = inter

        if merged[1] >= a:
            if merged[1] < b:
                merged[1] = b

        else:
            result.append([merged[0], merged[1]])
            merged[0], merged[1] = a, b

    result.append([merged[0], merged[1]])
    return result


merge([[1, 4], [2, 3]])

# 모범답안

# def merge(intervals: List[List[int]]) -> List[List[int]]:
#     # 시작 시간을 기준으로 구간 정렬
#     intervals.sort(key=lambda x: x[0])

#     merged = []

#     for interval in intervals:
#         # 만약 merged가 비어있거나, 이전 구간의 끝 시간이 현재 구간의 시작 시간보다 작다면
#         if not merged or merged[-1][1] < interval[0]:
#             merged.append(interval)
#         else:
#             # 겹치는 구간이라면, 이전 구간의 끝 시간을 현재 구간의 끝 시간과 비교하여 업데이트
#             merged[-1][1] = max(merged[-1][1], interval[1])

#     return merged
