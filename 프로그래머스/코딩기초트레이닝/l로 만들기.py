"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

알파벳 소문자로 이루어진 문자열 myString이 주어집니다. 알파벳 순서에서 "l"보다 앞서는 모든 문자를 "l"로 바꾼 문자열을 return 하는 solution 함수를 완성해 주세요.
"""


def solution(myString):
    return "".join(["l" if s < "l" else s for s in myString])
