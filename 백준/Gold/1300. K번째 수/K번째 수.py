# 백준 1300

# 문제
# 세준이는 크기가 N×N인 배열 A를 만들었다. 배열에 들어있는 수 A[i][j] = i×j 이다. 이 수를 일차원 배열 B에 넣으면 B의 크기는 N×N이 된다. B를 오름차순 정렬했을 때, B[k]를 구해보자.
#
# 배열 A와 B의 인덱스는 1부터 시작한다.
#
# 입력
# 첫째 줄에 배열의 크기 N이 주어진다. N은 105보다 작거나 같은 자연수이다. 둘째 줄에 k가 주어진다. k는 min(10^9, N2)보다 작거나 같은 자연수이다.
#
# 출력
# B[k]를 출력한다.
#
# 시간 제한 2s, k가 N^2보다 무조건 작아야 하기 때문에 2차원 배열을 깡으로 B에 저장해 sorting해서 찾는 거 보다는 BS로 찾아야 함(B는 정렬된 상태)

# middle / 1~N < K (K-1이 아닌)이라면 middle < K 이므로 start = middle + 1
# middle / 1~N > K 이라면 middle > K 이므로 end = middle - 1
# N*N 2차원 배열 A의 특성상 N행은 모두 N의 배수
# 그렇기 때문에 if) start > end,  middle / 1~N 의 갯수가 K-1일 경우 그 값이 B[K]!

# 입력
N = int(input())
K = int(input())


def binary_search_k(n,k):
    # 배열 A, B의 index: 1부터
    start = 1
    end = k

    # 결과
    result = 0

    # BS 조건
    while start<=end:
        # middle 보다 작은 수의 갯수 count
        count = 0

        middle = int((start + end) / 2)

        # i: 1~n for loop
        for i in range(1, n + 1):
            # n, middle/i 중 min
            count += min(int(middle / i), n)
        if count < k:
            start = middle + 1
        else:
            result = middle
            end = middle - 1

    return result

print(binary_search_k(N,K))




