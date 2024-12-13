"""
백준 알고리즘 사이트 코딩테스트 연습문제 10828번 풀이코드
"""

n = int(input())
stack = []
output = []

for _ in range(n):
    command = input()

    # push 명령어
    if command.find("push") != -1:
        value = command.split()[1]
        stack.append(int(value))

    # top 명령어
    elif command.find("top") != -1:
        if len(stack) == 0:
            output.append(-1)
        else:
            output.append(stack[-1])

    # pop 명령어
    elif command.find("pop") != -1:
        if len(stack) == 0:
            output.append(-1)
        else:
            output.append(stack.pop())

    # size 명령어
    elif command.find("size") != -1:
        output.append(len(stack))

    # empty 명령어
    elif command.find("empty") != -1:
        if len(stack) == 0:
            output.append(1)
        else:
            output.append(0)

for result in output:
    print(result)
