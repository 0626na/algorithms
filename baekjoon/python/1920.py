"""
백준 알고리즘 사이트 코딩테스트 연습문제 1920번 풀이코드
"""

n = int(input())
givenNumbers = set(map(int, input().split()))
m = int(input())
compareNumbers = list(map(int, input().split()))


for num in compareNumbers:
    if num in givenNumbers:
        print(1)
    else:
        print(0)
