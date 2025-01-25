"""
leetcode topInterview 150의 88. Merge Sorted Array 문제. Array, Two pointer, Sorting

"""

from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    nums1[:] = nums1[:m]
    nums1.extend(nums2)
    nums1.sort()


merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
