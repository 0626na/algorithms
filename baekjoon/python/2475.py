"""
백준 알고리즘 사이트 코딩테스트 연습문제 2475번 풀이코드
"""

numbers = list(map(int, input().split()))
sum = 0

for number in numbers:
    sum += pow(number, 2)

print(sum % 10)
