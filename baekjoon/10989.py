"""
백준 알고리즘 사이트 코딩테스트 연습문제 10989번 풀이코드

계수정렬을 활용했다.
"""

import sys

n = int(input())
counted = [0] * 10001
sorted_nums = []

for _ in range(n):
    inputNum = int(sys.stdin.readline().strip())
    counted[inputNum] += 1

for num in range(10001):
    if counted[num] == 0:
        continue
    for _ in range(counted[num]):
        print(num)
