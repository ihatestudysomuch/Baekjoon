# 백준 11399

# 입력
# 첫째 줄에 사람의 수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 Pi가 주어진다. (1 ≤ Pi ≤ 1,000)
#
# 출력
# 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.

# 0 < N < 1001 이므로 N^2해도 되니 사실 bubble, insertion, selection 아무거나 사용해도 상관없음 (제한 시간 1s)


# 입력
# TypeError 잘 봐 ..
# N = input()
N = int(input())
# TypeError 잘 봐...
# P = list(input().split())
P = list(map(int, input().split()))

# # 1. P 오름차순 정렬(insertion)
# for i in range(1, N):
#     # 삽입할 위치
#     point = i
#     value = P[i]
#     # i-1 ~ 0까지 1씩 감소, point 찾기
#     for j in range(i-1, -1, -1):
#         if P[j]< P[i]:
#             point = j+1
#             break
#         if j == 0:
#             point = 0;
#     # i ~ point 1씩 감소, insertion을 위해 당겨야함
#     for j in range(i, point, -1):
#         P[j] = P[j-1]
#     # point 위치에 value insertion
#     P[point] = value

# 1. P 오름차순 정렬 (sort())
P.sort(reverse=False)

# 2. 합배열 S
S = [0]*N
S[0] = P[0]

for i in range(1, N):
    # 합배열 공식
    S[i] = S[i-1] + P[i]

# 출력할 최소 합
output = 0

for i in range(N):
    output += S[i]

# 출력
print(output)