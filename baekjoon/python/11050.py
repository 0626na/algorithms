"""
백준 알고리즘 사이트 코딩테스트 연습문제 11050번 풀이코드
"""


def factorialN(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


n, k = map(int, input().split())

print(factorialN(n) // (factorialN(k) * factorialN(n - k)))
