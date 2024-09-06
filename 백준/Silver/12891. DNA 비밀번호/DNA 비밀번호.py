# 백준 12891
# use Sliding Window
# Sliding Window는 정해진 크기만큼 일정하게 이동하는 알고리즘
# S의 길이를 P의 길이로 유효한 DNA 비밀번호인지 확인
# S = 9, P = 8
# S: A A A A A A C G A
# P: A A A A A A C G만큼 끊어 유효한 비밀번호인지 판단

# 4칸의 비밀번호 checkList
checkList = [0] * 4
# 4칸의 현재 상태 myList
myList = [0] * 4
checkSecret = 0

# 옮기면서 들어오는 문자열의 처리
def myAdd(c):
    global checkList, myList, checkSecret
    # A C G T 모든 경우
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

# 옮기면서 없어지는 문자열을 처리
def myRemove(c):
    global checkList, myList, checkSecret

    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -= 1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1


# 문자열 길이 S, 비밀번호 길이 P
S, P = map(int, input().split())
# 문자열 string
string = list(input())
# check Sliding window
checkList = list(map(int, input().split()))
# 충족하는 결과 result
result = 0

for i in range(4):
    if checkList[i] == 0:
        checkSecret += 1

# 처음 문자열을 window(check)에 담았을 때
for i in range(P):
    myAdd(string[i])

if checkSecret == 4:
    result += 1

for i in range(P, S):
    j = i - P
    myAdd(string[i])
    myRemove(string[j])
    if checkSecret == 4:
        result += 1

print(result)



