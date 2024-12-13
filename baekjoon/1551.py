"""
백준 알고리즘 사이트 코딩테스트 연습문제 1551번 풀이코드
"""

nums = list(map(int, input().split()))
arr = list(map(int, input().split(",")))

n = nums[0]
k = nums[1]
length = len(arr)

for j in range(0, k):
    temp = []
    for i in range(0, length):
        if i == length - 1:
            break
        temp.append(arr[i + 1] - arr[i])
    arr = temp
    length = len(arr)


print(",".join(map(str, arr)))
