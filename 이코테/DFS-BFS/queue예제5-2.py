"""
큐 구조이해하기
구현을 위해서 deque 라이브러리 사용

5 삽입 - 2 삽입 - 3 삽입 - 7 삽입 - 삭제 - 1 삽입 - 4 삽입 - 삭제
"""

from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
