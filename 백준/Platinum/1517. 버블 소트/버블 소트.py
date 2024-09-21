# 백준 1517
# 문제
# N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.
#
# 버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다. 예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다. 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 500,000)이 주어진다. 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다. 각각의 A[i]는 0 ≤ |A[i]| ≤ 1,000,000,000의 범위에 들어있다.
#
# 출력
# 첫째 줄에 Swap 횟수를 출력한다

def merge_sort(start, end):
    global swap_count

    # 분할 불가능
    if end-start < 1:
        return

    # 분할 지점
    middle = int((start + end) / 2)

    # 계속 분할하여 분할 불가능에서 병합
    merge_sort(start, middle)
    merge_sort(middle + 1 , end)

    # 병합하여 만들어진 A를 temp에 저장
    for j in range(start, end + 1):
        temp[j] = A[j]

    k = start
    index_start = start
    index_middle = middle + 1

    while index_start<=middle and index_middle <= end:

        # 작은 값을 A에
        # 그 후 index를 오른쪽(+1)으로
        if temp[index_start] <= temp[index_middle]:
            A[k] = temp[index_start]
            k += 1
            index_start += 1
        else :
            A[k] = temp[index_middle]
            # Bubble sort에서 뒤의 수가 앞에 수보다 작으면 swap
            swap_count = swap_count + index_middle - k
            k += 1
            index_middle += 1

    # index start만 남았을 경우
    while index_start <= middle:
            A[k] = temp[index_start]
            k += 1
            index_start += 1
    # index_middle만 남았을 경우
    while index_middle <= end:
            A[k] = temp[index_middle]
            k += 1
            index_middle += 1

# 입력
N = int(input())
A = list(map(int, input().split()))
A.insert(0,0)

temp = [0] * int(N + 1)

swap_count = 0

# split() 할 거면 list로 구현해야함
# for i in range(1, N+1):
#     A[i] = int(input().split())

merge_sort(1, N)

print(swap_count)
