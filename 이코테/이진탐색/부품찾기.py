"""
이것이 코딩테스트다 이진탐색 예제 문제, 부품찾기

"""


def findParts():
    n = int(input())
    store = list(map(int, input().split()))
    m = int(input())
    require = list(map(int, input().split()))
    result = []

    store.sort()

    for r in require:
        output = binarySearch(store, r, 0, n - 1)
        result.append(output)

    print(" ".join(result))


def binarySearch(arr, finding, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == finding:
            return "yes"
        elif arr[mid] < finding:
            start = mid + 1
        else:
            end = mid - 1

    return "no"


findParts()
