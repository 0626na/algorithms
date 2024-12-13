"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

한 자리 정수로 이루어진 문자열 num_str이 주어질 때, 각 자리수의 합을 return하도록 solution 함수를 완성해주세요.
"""


def solution(num_str):
    return sum(int(i) for i in num_str)
