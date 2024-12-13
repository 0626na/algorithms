"""
재귀함수를 이해하기 위한 팩토리얼 예제
반복하는 방식과 재귀함수 방식으로 구현
"""


# 반복문으로 만든 팩토리얼
def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result *= i
    return result


# 재귀함수로 만든 팩토리얼
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)


print("반복문으로 만든 팩토리얼 ", factorial_iterative(5))
print("재귀함수로 만든 팩토리얼 ", factorial_recursive(5))
