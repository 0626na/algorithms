"""
leetcode Top Interview150 1. Two Sum. Array, Hash Table

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
"""

from typing import List

"""
풀이방법
- 해쉬 테이블을 선언
- 리스트 루프를 하면서 target과 각 리스트의 값인 num을 뺀다. 뺀 값인 rest가 없으면 현재 순회하는 num과 해당 num의 index를
  해쉬 테이블에 key:value로 넣는다.
- rest가 해쉬테이블에 있을경우 그 rest의 인덱스와 현재 순회중인 num의 인덱스를 리스트로 반환한다
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    nums_HashTable = {}

    for idx, num in enumerate(nums):
        rest = target - num
        if rest in nums_HashTable:
            return [nums_HashTable[rest], idx]
        nums_HashTable[num] = idx


twoSum([3, 3], 6)
