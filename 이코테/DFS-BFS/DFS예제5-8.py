"""
DFS 예제 코드
"""


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


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

print(visited)

dfs(graph, 1, visited)
