"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

정수 배열 arr과 정수 n이 매개변수로 주어집니다. 
arr의 길이가 홀수라면 arr의 모든 짝수 인덱스 위치에 n을 더한 배열을, arr의 길이가 짝수라면 arr의 모든 홀수 인덱스 위치에 n을 더한 배열을 return 하는 solution 함수를 작성해 주세요.
"""


def solution(arr, n):

    for idx in range(len(arr)):
        if len(arr) % 2 == 0 and idx % 2 != 0:
            arr[idx] += n
        if len(arr) % 2 != 0 and idx % 2 == 0:
            arr[idx] += n

    return arr


solution([49, 12, 100, 276, 33], 27)
