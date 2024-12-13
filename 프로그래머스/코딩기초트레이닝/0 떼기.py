"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

정수로 이루어진 문자열 n_str이 주어질 때, 
n_str의 가장 왼쪽에 처음으로 등장하는 0들을 뗀 문자열을 return하도록 solution 함수를 완성해주세요.

"""


def solution(n_str):
    answer = ""
    for idx, n in enumerate(n_str):
        if n != "0":
            answer = n_str[idx:]
            break

    return answer
