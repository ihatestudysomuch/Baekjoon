# 백준 2164
# python에서는 queue를 일반적으로 deque로 구현한다고 함!

import sys
from collections import deque

sys_input = sys.stdin.readline()

# 카드의 수 N
N = int(sys_input)
# deque 사용
deque = deque()

# i = 1 ~ N+1
# 카드 추가(정렬된 수로 추가)
for i in range(1, N+1):
    deque.append(i)

# deque의 길이 > 1
# 마지막 남은 카드의 수를 찾아야함
while len(deque) > 1:
    # 맨 위의 카드를 버림
    deque.popleft()
    # 맨 위의 카드를 맨 아래로 이동(맨 위의 카드를 N - 1이라 할 때, N - 1을 맨 아래에 append -> 아직 맨 위에 남아있는 N - 1을 popleft())
    deque.append(deque.popleft())

print(deque[0])
