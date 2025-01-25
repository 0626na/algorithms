"""
leetcode TopInterview 150
15. 3Sum
Array, Two Pointers, Sorting

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # 오름차순으로 정렬하면 찾기가 더 수월하다.
    n = len(nums)
    result = []

    for i in range(len(nums)):
        # i != j, i != k, and j != k 이부분을 만족시키기 위해서 탐색 포인터 i, 그리고 i 바로 다음인 left와
        # 리스트 끝인 right 이렇게 위치해서 탐색을 시작한다
        left, right = i + 1, n - 1

        # 위에서 오름차순으로 정렬 했기에 숫자가 양수면 그 이후 숫자도 전부 양수이기에 이후엔 0이 나올수가 없으므로 loop를 멈춘다.
        if nums[i] > 0:
            break

        # 이전 loop와 동일한 값은 이미 찾았기에 넘어간다. 문제에서는 중복 조합을 허용하지 않는다.
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        while left < right:
            total = nums[left] + nums[right] + nums[i]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # 현재 left 포인터의 값이 0이 되는걸 확인하고 이후 포인터의 값들이 지금과 같은 값이면 중복 조합이
                # 만들어 질수 있기에 같은 값들을 계속 스킵한다.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # right도 left에서 한것 처럼 동일한 이유로 같은 값들을 스킵한다.
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # 위에 skip은 중복된 값들의 마지막 인덱스 이기에 한번씩 이동해준다.
                left += 1
                right -= 1

            # 0보다 크기에 총합 크기를 줄이기 위해 right 포인터를 줄인다. 리스트가 오름차순이기에 right를 줄이면 값도 작아진다.
            elif total > 0:
                right -= 1
            else:
                left += 1

    return result


threeSum([-1, 0, 1, 2, -1, -4])
