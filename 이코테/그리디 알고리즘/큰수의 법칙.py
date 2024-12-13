# key point
# 연속 k번 더해질때 다른 값으로 변경하기
# 가장 큰수와 두번째로 큰수를 찾기

# numbers = list(map(int, input("N, M, K 순서대로 입력하기: ").split()))

# n = numbers[0]
# m = numbers[1]
# k = numbers[2]

# # 현재 몇번 더했는지 확인
# count_m = 0

# # 연속으로 몇번 더했는지 확인
# count_k = 1
# result = 0

# # 더하려는 숫자
# addedNumber = 0

# arr = list(map(int, input().split()))
# arr.sort()

# maxiumNumber = arr[len(arr) - 1]
# secondMaxiumNumber = arr[len(arr) - 2]
# addedNumber = maxiumNumber

# while count_m < m:

#     # 더하려는 숫자가 두번째로 큰수면 가장 큰수로 변경
#     if addedNumber == secondMaxiumNumber:
#         addedNumber = maxiumNumber

#     # 같은 수를 연속으로 더하는 횟수를 초과할 경우
#     if count_k > k:
#         if addedNumber == maxiumNumber:
#             addedNumber = secondMaxiumNumber
#         else:
#             addedNumber = maxiumNumber
#         count_k = 0

#     result += addedNumber
#     count_k += 1
#     count_m += 1

# print(result)


"""
밑에는 M의 최대수가 10,000을 넘기는 경우
이럴 경우에는 위의 방식으로는 시간 초과가 난다. 이럴 경우에는 일일히 루프를 돌지 않고, 반복되는 수열을 파악하여 가장 큰수를 더하는 횟수와 두번째로 큰수를 더하는 횟수를 구해서 계산한다.
"""

numbers = list(map(int, input("N, M, K 순서대로 입력하기: ").split()))

n = numbers[0]
m = numbers[1]
k = numbers[2]
result = 0

arr = list(map(int, input().split()))
arr.sort()

maxiumNumber = arr[len(arr) - 1]
secondMaxiumNumber = arr[len(arr) - 2]


"""
가장 큰수가 6이고 가장 작은수가 5일경우, k 값이 3이면 6 6 6 5 이런 수열을 반복한다. 그렇기에 수열의 길이는 k+1이다. 수열이 반복되는 횟수를 구하기 위해 m을 나눈다. 
그리고 거기에 k를 곱하면 가장 큰수를 더하는 횟수가 나온다. 그리고 이렇게 나온 반복횟수를 처음에 주어졌던 m에서 빼면 두번째로 큰수를 더하는 횟수가 된다.
"""

# 가장 큰수를 더하는 횟수
count = (m // (k + 1)) * k + m % (k + 1)

result += maxiumNumber * count
result += secondMaxiumNumber * (m - count)

print(result)
