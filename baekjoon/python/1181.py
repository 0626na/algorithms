"""
백준 알고리즘 사이트 코딩테스트 연습문제 1181번 풀이코드
"""


def merged_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merged_sort(arr[:mid])
    right = merged_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if len(left[i]) < len(right[j]):
            result.append(left[i])
            i += 1
        elif len(left[i]) > len(right[j]):
            result.append(right[j])
            j += 1
        else:
            if left[i] > right[j]:
                result.append(right[j])
                j += 1
            else:
                result.append(left[i])
                i += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


n = int(input())
vocas = []

for _ in range(0, n):
    voca = input()
    vocas.append(voca)

sortedVocas = merged_sort(list(set(vocas)))

for voca in sortedVocas:
    print(voca)
