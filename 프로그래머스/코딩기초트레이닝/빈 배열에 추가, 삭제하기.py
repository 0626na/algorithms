"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

아무 원소도 들어있지 않은 빈 배열 X가 있습니다. 
길이가 같은 정수 배열 arr과 boolean 배열 flag가 매개변수로 주어질 때, flag를 차례대로 순회하며 flag[i]가 true라면 X의 뒤에 arr[i]를 arr[i] x 2 번 추가하고, 
flag[i]가 false라면 X에서 마지막 arr[i]개의 원소를 제거한 뒤 X를 return 하는 solution 함수를 작성해 주세요.
"""


def solution(arr, flag):
    answer = []

    for idx, bl in enumerate(flag):
        if bl:
            answer += [arr[idx]] * (arr[idx] * 2)
        else:
            for _ in range(arr[idx]):
                if len(answer):
                    answer.pop()

    return answer
