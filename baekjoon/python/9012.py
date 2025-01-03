"""
백준 알고리즘 사이트 코딩테스트 연습문제 9012번 풀이코드
"""


# 괄호문자열 확인하는 스택함수
def psValidStack(psList):
    stack = []
    result = "NO"

    for ps in psList:
        # 열리지 않았는데 닫히는 괄호가 먼저 나오면 에러처리
        if ps == ")" and len(stack) == 0:
            stack.append("error")
            break
        # 닫히는 괄호를 보면 스택에서 open 값을 제거
        if ps == ")":
            stack.pop()
        # 괄호가 열리면 open
        if ps == "(":
            stack.append("open")

    if len(stack) == 0:
        result = "YES"

    return result


n = int(input())
results = []

for _ in range(n):
    ps = input()
    psList = list(ps)
    results.append(psValidStack(psList))

for result in results:
    print(result)
