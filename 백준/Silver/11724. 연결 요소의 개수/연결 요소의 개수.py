# 백준 11724

# 문제
# 방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
#
# 출력
# 첫째 줄에 연결 요소의 개수를 출력한다.

import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

# 입력
V, E = map(int, input().split())

# Graph에서 인접 리스트를 구현할 때 사용! 기억하자
# V, E = 3 -> A = [ [], [], [], [] ] 4개 생성
A = [[] for _ in range(V+1)]
# 방문 했는지 안 했는지 구분
visited = [False] * (V + 1)


def dfs(j):
    # 방문한 Voltex True
    visited[j] = True

    # 현재 Voltex에서 방문하지 않은 Voltex라면 다시 dfs 실행
    for i in A[j]:
        if not visited[i]:
            dfs(i)

# Edge 연결
for _ in range(E):
    s, e = map(int, input().split())

    # A[1] = [ [], [여기], [], [], [], [] ]
    # A[2] = [ [], [], [여기], [], [], [] ] -> 이런 식으로 기록
    # (1, 2) (2, 3) (1, 3)일 때,
    # A[1] = [ [], [2], [], [] ], A[2] = [ [], [2], [1], [] ]
    # A[2] = [ [], [2], [1,3], [] ] A[3] = [ [], [2], [1, 3], [2] ]
    # A[1] = [ [], [2, 3], [1, 3], [2] ] A[3] = [ [], [2, 3], [1, 3], [2,1] ]
    # 위와 같이 저장, 그래프의 인접리스트를 저장할 때 사용
    A[e].append(s)
    A[s].append(e)

# print(A)

count = 0

# 1~V까지 방문하지 않은 Voltex dfs
for i in range(1, V+1):
    if not visited[i]:
        count += 1
        dfs(i)

print(count)
