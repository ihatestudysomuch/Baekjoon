# 백준 1920
from dis import disco

# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.
#
# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다
#
# 시간 제한
# 1s

# 시간 제한이 빡셈..

# 입력
N = int(input())

A = list(map(int, input().split()))

# Binary Search는 sorting 해야만 가능
A.sort()

M = int(input())

range_A = list(map(int, input().split()))

# # 발견했는지 안 했는지
# discovery = False

# M만큼
for i in range(M):
    # 발견했는지 안 했는지
    discovery = False
    # 찾아야 할 수
    target = range_A[i]
    # index
    start = 0
    end = len(A) - 1
    # middle_index = int((start + end) / 2)
    #
    # # 중간값
    # middle_data = A[middle_index]
    # while 밖에서 하니까 무한루프 

    while start <= end:
        middle_index = int((start + end) / 2)

        # 중간값
        middle_data = A[middle_index]
        if middle_data > target:
            end = middle_index - 1
        elif middle_data < target:
            start = middle_index + 1
        else:
            discovery = True
            break
    if discovery:
        print(1)
    else:
        print(0)
