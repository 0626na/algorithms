"""
백준 알고리즘 사이트 코딩테스트 연습문제 28702번 풀이코드
"""

input1 = input()
input2 = input()
input3 = input()
inputToInt = 0

if input1.isdigit():
    inputToInt = int(input1)
    inputToInt += 3
if input2.isdigit():
    inputToInt = int(input2)
    inputToInt += 2
if input3.isdigit():
    inputToInt = int(input3)
    inputToInt += 1

if inputToInt % 3 == 0 and inputToInt % 5 == 0:
    print("FizzBuzz")
if inputToInt % 3 == 0 and inputToInt % 5 != 0:
    print("Fizz")
if inputToInt % 3 != 0 and inputToInt % 5 == 0:
    print("Buzz")
if inputToInt % 3 != 0 and inputToInt % 5 != 0:
    print(inputToInt)
