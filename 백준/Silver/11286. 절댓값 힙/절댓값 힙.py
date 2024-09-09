# 백준 11268
# Priority Queue와 Priority Queue의 정렬을 알아보자
# Priority Queue in python.. put(append), get(pop), get()[1] ..

import sys
from queue import PriorityQueue

# 입력한 결과를 한 번에 출력하기 위해서
sys_print = sys.stdout.write
sys_input = sys.stdin.readline

# 연산 횟수 N
N = int(sys_input())
# Priority Queue를 배열로 사용
priority_queue = PriorityQueue()
# 결과를 담을 result
result = []

# i: 0~N
for i in range(N):
    # queue에 넣을 값 x
    x = int(sys_input())
    if x == 0:
        # if priority_queue is null
        if priority_queue.empty():
            # 0 출력
            result.append("0")
            # sys_print("0\n")
        # if priority_queue is not null
        else:
            # priority_queue.get()[1]은 우선 순위의 값을 result에 추가
            result.append(str(priority_queue.get()[1]))
            # sys_print(str(priority_queue.get()[1]) + "\n")
    # x != 0
    else:
        # priority_queue에서 절댓값순으로 정렬, 절댓값이 같으면 크기 순(음수 순)으로 정렬
        priority_queue.put((abs(x), x))

# 한 번에 출력하기 위해
# \n.join(result)하게 되면 result의 모든 값을 \n으로 연결 후 마지막에 한 번에 출력
sys_print("\n".join(result)+ "\n")

# out of index
# for i in range(N):
#     sys_print(str(result[i]) + "\n")