"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

정수 n이 매개변수로 주어질 때, 다음과 같은 n × n 크기의 이차원 배열 arr를 return 하는 solution 함수를 작성해 주세요.
arr[i][j] (0 ≤ i, j < n)의 값은 i = j라면 1, 아니라면 0입니다.
"""


def solution(n):
    answer = []
    for i in range(n):
        arr = []
        for j in range(n):
            if i == j:
                arr.append(1)
            else:
                arr.append(0)
        answer.append(arr)

    return answer
