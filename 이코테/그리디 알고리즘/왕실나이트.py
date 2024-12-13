"""
이것이 취업을 위한 코딩테스트다 왕실나이트 문제

풀이방법
나이트는 총 8가지 경우의 수로 이동을 한다.
나이트가 이동 가능한 경우의 수를 전부 확인하여 체크하고 유효할시에 카운트를 증가시킨다.
"""

# 현재 나이트 위치
current = input()
# 가로부분
row = current[0]
# 세로부분
column = int(current[1])

count = 0

# 나이트가 이동할 수 있는 경우의 수

# 오른쪽으로 두칸 이동
if ord(row) + 2 <= ord("h"):
    # 아래로 한칸 이동
    if column + 1 <= 8:
        count += 1
    # 위로 한칸 이동
    if column - 1 >= 1:
        count += 1

# 왼쪽으로 두칸 이동
if ord(row) - 2 >= ord("a"):
    # 아래로 한칸 이동
    if column + 1 <= 8:
        count += 1
    # 위로 한칸 이동
    if column - 1 >= 1:
        count += 1

# 아래로 두칸 이동
if column + 2 <= 8:
    # 왼쪽으로 한칸이동
    if ord(row) - 1 >= ord("a"):
        count += 1
    # 오른쪽으로 한칸 이동
    if ord(row) + 1 <= ord("h"):
        count += 1

# 위로 두칸 이동
if column - 2 >= 1:
    # 왼쪽으로 한칸이동
    if ord(row) - 1 >= ord("a"):
        count += 1
    # 오른쪽으로 한칸 이동
    if ord(row) + 1 <= ord("h"):
        count += 1


print(count)
