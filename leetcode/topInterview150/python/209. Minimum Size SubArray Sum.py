"""
leetcode Top Interview 150 문제 중 Sliding Window 카테고리의 문제

Given an array of positive integers 'nums' and a positive integer 'target', return the minimal length of a 
'subarray' whose sum is greater than or equal to 'target'. If there is no such 'subarray', return 0 instead.
"""

nums = [1, 1, 1, 1, 7]
target = 7
min_length = float("inf")
currentSum = 0
start = 0  # 슬라이싱 윈도우를 위한 시작과 끝 인덱스 변수

for end in range(len(nums)):
    currentSum += nums[end]
    while currentSum >= target:
        min_length = min(min_length, end - start + 1)
        currentSum -= nums[start]
        start += 1


print(0 if min_length == float("inf") else min_length)
