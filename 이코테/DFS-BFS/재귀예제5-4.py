"""
재귀의 개념을 이해하기 위한 예제 함수
100번째 호출시에 멈추도록 한다. 재귀함수는 조건을 달아주지 않으면 무한히 호출되기에 반드시 조건이 있어야한다
"""


def recursive_function(i):
    if i == 100:
        return
    print(f"{i}번째 재귀함수, {i+1}번째 재귀함수를 호출한다")
    recursive_function(i + 1)
    print(f"{i}번째 재귀함수 종료")


recursive_function(1)
