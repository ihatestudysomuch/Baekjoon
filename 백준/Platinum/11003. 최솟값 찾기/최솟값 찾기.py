# 백준 11003

# input:
# 12 3
# 1 5 2 3 6 2 3 7 3 5 2 6
#
# output:
# 1 1 1 2 2 2 2 2 3 3 2 2

from collections import deque

# 갯수 N, 슬라이딩 윈도우 크기 L
N, L = map(int, input().split())
# N개의 수 input_n
input_n = list(map(int, input().split()))
# deque 생성
deque = deque()

for i in range(N):
    # input_n 보다 큰 값은 deque에서 제거하여 정렬
    # deque[-1][0] = deque의 마지막 값
    while deque and deque[-1][0] > input_n[i]:
        deque.pop()
    deque.append((input_n[i], i))
    if deque[0][1] <= i-L:
        deque.popleft()
    # deque[0][0]은 제일 첫 번째 값으로 정렬되어있으니 최소값
    print(deque[0][0], end=" ")


