"""
leetcode Top Interview 150의 169. Majority Element. Array, Sorting, Hash Table, Counting

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
"""

from typing import List


"""
풀이 알고리즘

1. nums 리스트 데이터로 딕셔너리를 만든다. 딕셔너리에는 key는 각 리스트의 요소, value는 각 요소들의 리스트에 존재하는 갯수로 만든다.
2. 딕셔너리를 만들고나서 딕셔너리에서 가장 큰 value를 가진 key를 반환한다.
"""


def majorityElement(nums: List[int]) -> int:
    nums_dictionary = {}

    for n in nums:
        if n in nums_dictionary:
            nums_dictionary[n] += 1
            continue
        nums_dictionary[n] = 1

    return max(nums_dictionary, key=nums_dictionary.get)
