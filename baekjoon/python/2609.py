"""
백준 알고리즘 사이트 코딩테스트 연습문제 2609번 풀이코드
"""

nums = list(map(int, input().split()))

a = nums[0]
b = nums[1]

while 1:
    if b == 0:
        break
    a, b = b, a % b

print(a)
print(int((nums[0] * nums[1]) / a))
