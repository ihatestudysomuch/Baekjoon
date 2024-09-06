# 백준 1253
# Two-Pointer(크면 큰 index 낮추기, 작으면 작은 index 낮추기)

# input:
# 10
# 1 2 3 4 5 6 7 8 9 10
#
# output:
# 8

import sys

input = sys.stdin.readline
# 1번 째 줄 N(수의 개수)
N = int(input())
# 2번 째 줄 An(N의 값)
An = list(map(int, input().split()))

An.sort()

# 결과 count
count = 0

for k in range(N):
    result = An[k]
    i = 0
    j = N - 1
    # Two-pointer 공식
    while i < j:
        # count += 1(정답 경우)
        if An[i] + An[j] == result:
            if i != k and j != k:
                count += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        # 큰 경우
        elif An[i] + An[j] > result:
            j -= 1
        else:
            i += 1

print(count)





