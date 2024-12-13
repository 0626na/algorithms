"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

0번부터 n - 1번까지 n명의 학생 중 3명을 선발하는 전국 대회 선발 고사를 보았습니다. 
등수가 높은 3명을 선발해야 하지만, 개인 사정으로 전국 대회에 참여하지 못하는 학생들이 있어 참여가 가능한 학생 중 등수가 높은 3명을 선발하기로 했습니다.
각 학생들의 선발 고사 등수를 담은 정수 배열 rank와 전국 대회 참여 가능 여부가 담긴 boolean 배열 attendance가 매개변수로 주어집니다. 
전국 대회에 선발된 학생 번호들을 등수가 높은 순서대로 각각 a, b, c번이라고 할 때 10000 × a + 100 × b + c를 return 하는 solution 함수를 작성해 주세요.
"""

"""
풀이 알고리즘

1. 학생이 참석여부를 확인한다. 불참이면 바로 다음 학생으로 넘어간다.
2. 참석하는 학생일 경우, 3순위 안에 들어오는지를 확인한다.
3. 3명이 채워지면 순회를 멈추고 값을 계산하여 return
여기서 학생번호는 리스트의 Index이다.
"""


def solution(rank, attendance):
    enabled = []
    students = []
    for idx, attend in enumerate(attendance):
        if not attend:
            continue
        if len(enabled) < 3:
            enabled += [rank[idx]]
        elif len(enabled) == 3:
            enabled += [rank[idx]]
            enabled.sort()
            enabled.pop()

    enabled.sort()
    for r in enabled:
        students.append(rank.index(r))
    a, b, c = students

    return 10000 * a + 100 * b + c


solution([6, 1, 5, 2, 3, 4], [True, False, True, False, False, True])
