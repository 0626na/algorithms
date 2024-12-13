"""
백준 알고리즘 사이트 코딩테스트 연습문제 14652번 풀이코드
"""

nums = list(map(int, input().split()))


n = nums[0]  # row
m = nums[1]  # column
k = nums[2]

print(k // m, k % m)
