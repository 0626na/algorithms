"""
약수

문제
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

출력
첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.

예제 입력 1 
2
4 2
예제 출력 1 
8
예제 입력 2 
1
2
예제 출력 2 
4
예제 입력 3 
6
3 4 2 12 6 8
예제 출력 3 
24
예제 입력 4 
14
14 26456 2 28 13228 3307 7 23149 8 6614 46298 56 4 92596
예제 출력 4 
185192

출처
문제를 번역한 사람: baekjoon
빠진 조건을 찾은 사람: doju
어색한 표현을 찾은 사람: jh05013
"""

n = int(input())
factors = list(map(int, input().split()))
result = 0

factors.sort()

if len(factors) == 1:
    result = factors[0] ** 2
else:
    result = factors[0] * factors[-1]

print(result)
