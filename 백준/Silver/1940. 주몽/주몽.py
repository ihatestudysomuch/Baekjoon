# 백준 1940
# Use To-Pointer

# 재료의 개수 N (1 < N < 15,000)
N = int(input())
# 두 재료 번호의 합 M (1 < M < 10,000,000)
M = int(input())
# N의 번호 리스트 A, map: 반복 가능 객체(리스트 같은)요소에 변환된 결과 반환, split() 으로 공백 쪼개기
L = list(map(int, input().split()))
# N의 번호가 항상 오름차순 정렬이 안되기 때문에 정렬
L.sort()

# 정답 개수
count = 0

start_index = 0;
# 최소 0
end_index = N - 1;

while start_index < end_index:
    # 두 재료 번호의 합 < M
    if L[start_index] + L[end_index] < M:
        start_index += 1
    # 두 재료 번호의 합 > M
    elif L[start_index] + L[end_index] > M:
        end_index -= 1
    # 두 재료 번호의 합 = M (정답)
    else:
        count += 1
        start_index += 1
        end_index -= 1

print(count)