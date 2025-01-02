"""
이것이 코딩테스트다 이진탐색 문제. 떡볶이 떡 만들기
"""


def bestHight():
    n, m = map(int, input().split())
    elements = list(map(int, input().split()))

    elements.sort()
    end = elements[-1]
    start = 0
    restSum = 0

    while start <= end:
        mid = (start + end) // 2
        restSum = 0
        for el in elements:
            if el >= mid:
                restSum += el - mid
        if restSum == m:
            return mid
        if restSum > m:
            start = mid + 1
        elif restSum < m:
            end = mid - 1


print(bestHight())
