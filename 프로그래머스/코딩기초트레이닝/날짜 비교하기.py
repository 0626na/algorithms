"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

정수 배열 date1과 date2가 주어집니다. 두 배열은 각각 날짜를 나타내며 [year, month, day] 꼴로 주어집니다. 각 배열에서 year는 연도를, month는 월을, day는 날짜를 나타냅니다.
만약 date1이 date2보다 앞서는 날짜라면 1을, 아니면 0을 return 하는 solution 함수를 완성해 주세요.
"""

from datetime import datetime


def solution(date1, date2):
    d1 = datetime.strptime(f"{date1[0]:04d}-{date1[1]}-{date1[2]}", "%Y-%m-%d")
    d2 = datetime.strptime(f"{date2[0]:04d}-{date2[1]}-{date2[2]}", "%Y-%m-%d")

    return 1 if d1 < d2 else 0


solution([2021, 12, 28], [1, 12, 28])
