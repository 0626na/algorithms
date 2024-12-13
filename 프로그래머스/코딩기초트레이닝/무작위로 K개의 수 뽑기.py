"""
프로그래머스 코딩테스트 기초트레이닝 part의 문제

랜덤으로 서로 다른 k개의 수를 저장한 배열을 만드려고 합니다. 적절한 방법이 떠오르지 않기 때문에 일정한 범위 내에서 무작위로 수를 뽑은 후, 
지금까지 나온적이 없는 수이면 배열 맨 뒤에 추가하는 방식으로 만들기로 합니다.
이미 어떤 수가 무작위로 주어질지 알고 있다고 가정하고, 실제 만들어질 길이 k의 배열을 예상해봅시다.
정수 배열 arr가 주어집니다. 문제에서의 무작위의 수는 arr에 저장된 순서대로 주어질 예정이라고 했을 때, 
완성될 배열을 return 하는 solution 함수를 완성해 주세요.

단, 완성될 배열의 길이가 k보다 작으면 나머지 값을 전부 -1로 채워서 return 합니다.
"""

"""
풀이 알고리즘

1. arr 배열을 하나씩 꺼내서 return 하는 배열에 해당 값이 있는지 확인한다. 있으면 추가하고 없으면 그냥 넘어간다.
2. 배열의 길이가 k와 같으면 그대로 순회를 종료하고 나와서 배열을 return 한다
3. arr 배열을 전부 순회했는데도 k보다 길이가 짦으면 모자란 만큼의 길이를 -1로 채워서 넣고 return 한다.
"""


def solution(arr, k):
    answer = []
    setArr = set()

    for s in arr:
        if s not in setArr:
            setArr.add(s)
            answer += [s]
        if len(setArr) == k:
            return answer

    answer += [-1] * (k - len(setArr))
    return answer
