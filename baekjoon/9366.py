"""
백준 알고리즘 사이트 코딩테스트 연습문제 9366번 풀이코드
"""

count = int(input())
result = []

for i in range(0, count):
    sides = list(map(int, input().split()))
    sides.sort()

    # 삼각형 안됨
    if sides[0] + sides[1] <= sides[2]:
        result.append(f"Case #{i+1}: invalid!")
        continue

    # 정삼각형
    if sides[0] == sides[1] == sides[2]:
        result.append(f"Case #{i+1}: equilateral")
        continue

    # 이등변 삼각형
    if sides[0] == sides[1] or sides[1] == sides[2]:
        result.append(f"Case #{i+1}: isosceles")
        continue

    # 부등변 삼각형
    if sides[0] != sides[1] != sides[2]:
        result.append(f"Case #{i+1}: scalene")
        continue


for sentence in result:
    print(sentence)
