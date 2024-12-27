"""
leetcode TopInterview 150 228. Summary Ranges. Array

You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.
"""

from typing import List

"""
풀이방법
- 시작부분에 해당하는 인덱스 포인터 start, 마지막 부분에 해당하는 인덱스 포인터 end를 설정한다
- 순회를 하면서 현재 인덱스와 바로 다음 인덱스를 뺄때 1이 아닌 그 이상 값이 나오면 거기서 멈추고 start와 end 인덱스 값까지의 범위의 숫자값을 리스트에 입력한다.
"""


def summaryRanges(nums: List[int]) -> List[str]:
    result = []
    start, end = 0, 0

    for i in range(len(nums)):

        if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
            if end - start == 0:
                result.append(f"{nums[start]}")
            else:
                result.append(f"{nums[start]}->{nums[end]}")
            end = i + 1
            start = i + 1
        else:
            end += 1

    return result


summaryRanges([0, 1, 2, 4, 5, 7])
