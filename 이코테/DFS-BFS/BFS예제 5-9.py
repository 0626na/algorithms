"""
BFS 예제코드
"""

from collections import deque


ttt = deque([1, 2, 3])


def bfs(graph, start, visited):
    queue = deque([start])

    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    # 노드를 1번부터 사용할것이기에 인덱스 0은 사용하지 않는다.
    [],
    [2, 3, 8],  # 1번노드의 연결상태
    [1, 7],  # 2번노드의 연결상태
    [1, 4, 5],  # 3번노드의 연결상테
    [3, 5],  # 4번노드의 연결상태
    [3, 4],  # 5번노드의 연결상태
    [7],  # 6번노드의 연결상태
    [2, 6, 8],  # 7번노드의 연결상태
    [1, 7],  # 8번노드의 연결상태
]

# 각 노드마다 방문상태 체크
visited = [False] * 9

# bfs(graph, 1, visited)
print(ttt)
