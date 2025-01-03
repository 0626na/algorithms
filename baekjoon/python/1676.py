"""
백준 알고리즘 사이트 코딩테스트 연습문제 1676번 풀이코드
"""


def factorialN(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


n = int(input())
count = 0

factorialNumber = factorialN(n)
arr = list(f"{factorialNumber}")
arr.reverse()

for num in arr:
    if int(num) == 0:
        count += 1
    else:
        break

print(count)
