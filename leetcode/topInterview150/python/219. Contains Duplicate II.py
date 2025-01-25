"""
leetcode top interview 150 219. Contains Duplicate II. Array, Hash Table ,Sliding Window

Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
0 <= k <= 105
"""

from typing import List

"""
풀이방법
- 해시테이블을 하나 두고, key를 리스트 요소로하고 value를 해당 값의 인덱스로 한다.
- 현재 순회중인 인덱스의 요소값이 해시테이블에 없다면 해시테이블에 추가한다
- 만약 있다면 현재 인덱스와 현재 인덱스의 요소값과 같은 key의 value를 빼고 절대값을 구한다. 그리고 이 절대값이 k보다 작거나 같은지 확인한다.
- 만약 조건을 일치하면 True를 주고 loop를 빠져나온다.
- 값은 같지만 조건이 맞지 않으면 해시테이블을 현재 인덱스로 갱신한다.
"""


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    table = {}
    result = False

    for i in range(len(nums)):
        if not nums[i] in table:
            table[nums[i]] = i
            continue

        if abs(i - table[nums[i]]) <= k:
            result = True
            break
        table[nums[i]] = i

    return result


containsNearbyDuplicate([1, 0, 1, 1], 1)
