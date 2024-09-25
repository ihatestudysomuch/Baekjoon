# 백준 2023

# 문제
# 수빈이가 세상에서 가장 좋아하는 것은 소수이고, 취미는 소수를 가지고 노는 것이다. 요즘 수빈이가 가장 관심있어 하는 소수는 7331이다.
#
# 7331은 소수인데, 신기하게도 733도 소수이고, 73도 소수이고, 7도 소수이다. 즉, 왼쪽부터 1자리, 2자리, 3자리, 4자리 수 모두 소수이다! 수빈이는 이런 숫자를 신기한 소수라고 이름 붙였다.
#
# 수빈이는 N자리의 숫자 중에서 어떤 수들이 신기한 소수인지 궁금해졌다. N이 주어졌을 때, 수빈이를 위해 N자리 신기한 소수를 모두 찾아보자.
#
# 입력
# 첫째 줄에 N(1 ≤ N ≤ 8)이 주어진다.
#
# 출력
# N자리 수 중에서 신기한 소수를 오름차순으로 정렬해서 한 줄에 하나씩 출력한다.

import sys
sys.setrecursionlimit(10000)

# 입력(자리수)
N = int(input())

# 소수인지 아닌지 판단
def question_prime(number):
    k = int((number / 2) + 1)

    for i in range(2, k):
        if number % i == 0:
            # 나누어 떨어지면 소수가 아님
            return False
    return True

def dfs(number):
    # number의 자릿수 == N
    if len(str(number)) == N:
        print(number)
    else:
        # 자릿수를 늘린 후 1~9까지 더 했을 때 소수라면 자릿수를 늘리고 그 수를 더함
        # 그리고 그 수가 소수인지 다시 판단(recursive call dfs)
        for i in range(1, 10):
            # 더하는 수가 짝수면 소수x
            if i % 2 ==0:
                continue
            if question_prime(number * 10 + i):
                dfs(number * 10 + i)

# 첫 번째 자리가 소수인 2, 3, 5, 7로 소수 늘려가기
dfs(2)
dfs(3)
dfs(5)
dfs(7)