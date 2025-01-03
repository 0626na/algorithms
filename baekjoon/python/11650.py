"""
백준 알고리즘 사이트 코딩테스트 연습문제 11650번 풀이코드
"""

n = int(input())
nums = []

for _ in range(n):
    x, y = map(int, input().split())
    nums.append({"x": x, "y": y})

nums.sort(key=lambda n: (n["x"], n["y"]))

for num in nums:
    print(num["x"], num["y"])
