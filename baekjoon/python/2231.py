"""
백준 알고리즘 사이트 코딩테스트 연습문제 2231번 풀이코드
"""

n = int(input())
maker = 0

for i in range(1, n + 1):
    digitSum = i + sum(map(int, list(str(i))))
    if n == digitSum:
        maker = i
        break

print(maker)
