"""
백준 알고리즘 사이트 코딩테스트 연습문제 20540번 풀이코드
"""

mbtiInput = input()
result = []

mbti = list(mbtiInput)

for ch in mbti:
    if ch == "E":
        result.append("I")
    elif ch == "I":
        result.append("E")

    if ch == "S":
        result.append("N")
    elif ch == "N":
        result.append("S")

    if ch == "T":
        result.append("F")
    elif ch == "F":
        result.append("T")

    if ch == "J":
        result.append("P")
    elif ch == "P":
        result.append("J")

print("".join(result))
