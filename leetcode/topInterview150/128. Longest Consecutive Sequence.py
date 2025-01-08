"""
leetcode TopInterview150
128. Longest Consecutive Sequence
Array, Hash Table, Union Find


Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from typing import List


def longestConsecutive(nums: List[int]) -> int:
    hash = set(nums)
    consecutive = 0
    count = 0

    for n in hash:
        count = 1
        if n - 1 in hash:
            continue

        while True:
            if not n + 1 in hash:
                break
            n += 1
            count += 1

        if consecutive < count:
            consecutive = count

    return consecutive


longestConsecutive(
    [4, 0, -4, -2, 2, 5, 2, 0, -8, -8, -8, -8, -1, 7, 4, 5, 5, -4, 6, 6, -3]
)
