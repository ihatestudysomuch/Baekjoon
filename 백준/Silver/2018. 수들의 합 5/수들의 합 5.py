# 백준 2018
# Use To-Pointer
# To-Pointer O(N)

# scanf 같음, 입력할 수 n
n=int(input())

start_index = 1
end_index = 1
# 만약 15의 경우의 수를 찾을 때, 15 단독이 가능 하므로 count=1로 초기화
count = 1
# 연속하는 자연수들의 합
result = 1

# end_index = n(만약 n = 15, 15 단독으로 가정했을 때를 대비해 count = 1로 초기화) 제외
while end_index != n:
    if result == n:
        count += 1
        end_index += 1
        result += end_index
    elif result > n:
        result -= start_index
        start_index += 1
    else:
        end_index += 1
        result += end_index

print(count)