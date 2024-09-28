# 백준 1260

# 문제
# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
#
# 입력
# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.
#
# 출력
# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque

# 입력
# N: 수의 갯수, M = edge, V = 시작 수
N, M, V = map(int, input().split())

# dfs, bfs에서 자주 쓰임 A = [ [1], [2], [3] ] 형태
A = [[] for _ in range(N+1)]

# edge 연결
for _ in range(M):

    s, e = map(int, input().split())

    # undirected graph
    A[s].append(e)
    A[e].append(s)

for i in range(N+1):
    A[i].sort()

visited = [False] * (N + 1)

# DFS
def dfs(v):

    # 이런 출력법이 있는 거 같음 알아보자
    print(v, end=' ')

    visited[v] = True

    for i in A[v]:
        if not visited[i]:
            dfs(i)

# BFS
def bfs(v):
    queue = deque()

    # 방문한 수 queue에 넣기
    queue.append(v)

    visited[v] = True

    # queue에 node가 존재 할 동안(없으면 탐색 끝)
    while queue:

        now = queue.popleft()
        print(now, end=' ')

        for i in A[now]:
            if not visited[i]:
                # queue에 넣기 전 방문했다고 표시
                visited[i] = True
                queue.append(i)



# for i in range(N+1):
#     print(A[i])

# 출력
dfs(V)
# 초기화
print()
visited = [False] * (N+1)
bfs(V)