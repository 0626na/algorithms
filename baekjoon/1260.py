"""
백준 알고리즘 1260번 문제 DFS와 BFS
"""

from collections import deque

# n: 노드 갯수
# m: 간선 갯구
# v: 탐색을 시작할 노드
n, m, v = map(int, input().split())

# graph를 표시하기 위한 2차원 리스트
graph = [[] for _ in range(n + 1)]

# visited1은 dfs 알고리즘, visited2는 bfs 알고리즘
visited1 = [False] * (n + 1)
visited2 = [False] * (n + 1)

# 각 graph의 노드간 관계를 설정
for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    graph[x].sort()
    graph[y].sort()


def dfs(graph, k, visited):
    visited[k] = True
    print(k, end=" ")
    for i in graph[k]:
        if not visited[i]:
            dfs(graph, i, visited)


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


dfs(graph, v, visited1)
print()
bfs(graph, v, visited2)
