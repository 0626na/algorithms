"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

문자열 배열 strArr이 주어집니다. 
strArr의 원소들을 길이가 같은 문자열들끼리 그룹으로 묶었을 때 가장 개수가 많은 그룹의 크기를 return 하는 solution 함수를 완성해 주세요.
"""

from collections import Counter


"""
풀이 알고리즘

파이썬의 Counter 클래스를 이용한다. Counter는 여러 요소들의 빈도수를.. 얼마나 자주 나타났는지를 그 빈도수를 저장하는 딕셔너리이다.
Counter로 각 문자열의 길이를 구하고, 그 길이값들이 얼마나 자주 나타났는지를 전부 저장하여 Counter 오브젝트에 저장한다.
Counter 오브젝트에서 values() 내장함수로 값들만 추출한다. 그리고 max 함수로 이중에 가장 큰 값을 가져온다.
"""


def solution(strArr):
    return max(Counter(len(s) for s in strArr).values())


solution(["a", "bc", "d", "efg", "hi"])
