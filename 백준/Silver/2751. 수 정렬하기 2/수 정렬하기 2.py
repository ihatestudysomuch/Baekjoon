# 백준 2751

# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

# merge로 풀어보자

import sys
input = sys.stdin.readline
print = sys.stdout.write

def merge_sort(first, second):
    # 3 5 1 2 9 6 4 3  -> 3/5/1/2/9/6/4/3/ 의 경우, first == second
    if second - first < 1:
        return

    # 중간 지점 m
    middle = int((first + second) / 2)

    merge_sort(first, middle)
    merge_sort(middle + 1, second)

    # A 배열을 temp 배열에 저장
    # 이 말은 병합된 배열 A를 temp에 저장 ... 병합 temp에 저장.. 반복
    for j in range(first, second + 1):
        temp[j] = A[j]

    one = first
    index1 = first
    index2 = middle + 1

    while index1 <= middle and index2 <= second:
        # 오름차순 정렬이기 때문에 작은 수 부터 저장
        # 3 5 1 2 9 6 4 3, 3/5/1/2/9/6/4/3 -> 3 5/1 2/6 9/3 4 -> .. 1 2 3 5 / 3 4 6 9 -> 1 2 3 3 4 5 6 9 이렇게 병합 정렬
        # 3 5/1 2/6 9/3 4 이 경우, 네 덩이에서 각각 temp[index1]: 3 1 6 3, temp[index2]: 5 2 9 3, 정렬 하면 1 2 3 5  / 3 4 6 9로 병합 정렬 된다.
        if temp[index1] > temp[index2]:
            A[one] = temp[index2]
            one += 1
            index2 += 1
        else:
            A[one] = temp[index1]
            one += 1
            index1 += 1
    # index2가 이동 할 곳이 없고 index1만 남은 경우
    while index1 <= middle:
        A[one] = temp[index1]
        one += 1
        index1 += 1
    # index1이 이동 할 곳이 없고 index2만 남은 경우
    while index2 <= second:
        A[one] = temp[index2]
        one += 1
        index2 += 1


# 입력
N = int(input())
A = [0] * int(N + 1)
temp = [0] * int(N + 1)

for i in range(1, N + 1):
    A[i] = int(input())

merge_sort(1, N)

for i in range(1, N + 1):
    print(str(A[i]) + '\n')

