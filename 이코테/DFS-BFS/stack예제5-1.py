"""
스택 자료구조의 예제
간단하게 스택이 어떤 것인지를 알아보고 구현해본다.

5 삽입 - 2 삽입 - 3 삽입 - 7 삽입 - 삭제 - 1 삽입 - 4 삽입 - 삭제
위의 과정을 스택자료구조로 해본다.
"""

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)

print(stack)

stack.pop()

print(stack)

stack.append(1)
stack.append(4)
stack.pop()

print(stack)
