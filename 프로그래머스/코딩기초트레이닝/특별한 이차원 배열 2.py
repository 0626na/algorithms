"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

n × n 크기의 이차원 배열 arr이 매개변수로 주어질 때, arr이 다음을 만족하면 1을 아니라면 0을 return 하는 solution 함수를 작성해 주세요.
0 ≤ i, j < n인 정수 i, j에 대하여 arr[i][j] = arr[j][i]
"""


def solution(arr):

    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1


solution(
    [[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]
)
