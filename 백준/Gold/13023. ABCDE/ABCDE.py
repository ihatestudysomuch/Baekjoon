# 백준 13023

# 문제
# BOJ 알고리즘 캠프에는 총 N명이 참가하고 있다. 사람들은 0번부터 N-1번으로 번호가 매겨져 있고, 일부 사람들은 친구이다.
#
# 오늘은 다음과 같은 친구 관계를 가진 사람 A, B, C, D, E가 존재하는지 구해보려고 한다.
#
# A는 B와 친구다.
# B는 C와 친구다.
# C는 D와 친구다.
# D는 E와 친구다.
# 위와 같은 친구 관계가 존재하는지 안하는지 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 사람의 수 N (5 ≤ N ≤ 2000)과 친구 관계의 수 M (1 ≤ M ≤ 2000)이 주어진다.
#
# 둘째 줄부터 M개의 줄에는 정수 a와 b가 주어지며, a와 b가 친구라는 뜻이다. (0 ≤ a, b ≤ N-1, a ≠ b) 같은 친구 관계가 두 번 이상 주어지는 경우는 없다.
#
# 출력
# 문제의 조건에 맞는 A, B, C, D, E가 존재하면 1을 없으면 0을 출력한다.

# A - B - C - D - E 로 이어지므로 graph depth = 5 일 때 1, 아니면 0 (0 ~ N-1이니까 depth를 0~4로 해야하나..?)

import sys
sys.setrecursionlimit(10000)

# 입력 Vortex, Edge
V, E = map(int, input().split())
# Graph
G = [[] for _ in range(V + 1)]
# 방문함?
visited = [False] * (V + 1)
# depth == 5?
complete = False

def dfs(number, depth):
    global complete

    # 만족하면
    if depth == 5:
        complete = True
        return

    # dfs 시작시 방문
    visited[number] = True

    for j in G[number]:
        if not visited[j]:
            dfs(j, depth + 1)
    # Backtracking 방지
    visited[number] = False

# 입력한 수를 Edge로 연결(undirected -> 두 수를 왔다갔다 가능 -> 둘 다 연결)
for _ in range(E):
    s, e = map(int, input().split())

    G[s].append(e)
    G[e].append(s)

for i in range(V):
    dfs(i, 1)
    if complete:
        break

if complete:
    print(1)
else:
    print(0)




















