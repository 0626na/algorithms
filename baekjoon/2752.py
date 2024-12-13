"""
백준 알고리즘 사이트 코딩테스트 연습문제 2752번 풀이코드
"""

nums = list(map(int, input().split()))

for i in range(0, 2):
    for j in range(0, 2 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(" ".join(map(str, nums)))
