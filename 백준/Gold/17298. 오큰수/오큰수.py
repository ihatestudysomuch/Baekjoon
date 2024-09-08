# 백준 17298
# 오큰수(큰 수가 오른쪽에 있을 때 가장 왼쪽에 있는 수) 찾기

import sys

# 수열 길이
N = int(sys.stdin.readline())
# 오큰수를 저장할 result
# 오큰수가 존재하지 않는 마지막 값은 -1로 고정
result = [0]*N
# 수열 A
A = list(map(int, sys.stdin.readline().split()))
# 저장할 stack
# 첫 번째 index = 0은 stack에 존재
stack = [0]

# 잊지마! index를 stack에 담아 수를 비교하는 거야!
# 정렬할 필요 x -> 정렬하면 모든 오른쪽의 수가 오큰수
for i in range(1, N):
    # stack is nor null and A[top] < A[i]
    # stack[-1]이 top인 듯
    # 쉽게 생각하자 top의 index가 가리키는 수열 = A[stack[-1]]
    # A의 0~N까지 i번째 수열 A[i] (1번 쩨: A[0], 2번 째: A[1] ..)
    while stack and A[stack[-1]] < A[i]:
        # 그 수를 result에 저장
        result[stack.pop()] = A[i]
    # 그 조건이 아니라면 append(i)
    stack.append(i)

while stack:
    result[stack.pop()] = -1

print(*result)