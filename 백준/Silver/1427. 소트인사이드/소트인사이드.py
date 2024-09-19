# 백준 1427
# O(n^2) 효율적이지 않음
# 근데 굳이 내가 python의 sort()를 사용하지 말아야 할 이유가 있나...? (O(nlogn) 인데..)

import sys
print = sys.stdout.write

# 정렬 할 수 A
A = list(input())

# for i in range(len(A)):
#     # 가장 큰 수 max, 처음부터 출발
#     Max = i
#     # 다음 수 j부터
#     for j in range(i+1, len(A)):
#         if A[j] > A[Max]:
#             Max = j
#     # 내림차순 정렬이기 때문에 Max가 처음으로
#     if A[i] < A[Max]:
#         temp = A[i]
#         A[i] = A[Max]
#         A[Max] = temp
#
# for i in range(len(A)):
#     print(A[i])

A.sort(reverse=True)

for i in range(len(A)):
    print(A[i])