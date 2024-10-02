# 백준 2343

# 문제
# 강토는 자신의 기타 강의 동영상을 블루레이로 만들어 판매하려고 한다. 블루레이에는 총 N개의 강의가 들어가는데, 블루레이를 녹화할 때, 강의의 순서가 바뀌면 안 된다. 순서가 뒤바뀌는 경우에는 강의의 흐름이 끊겨, 학생들이 대혼란에 빠질 수 있기 때문이다. 즉, i번 강의와 j번 강의를 같은 블루레이에 녹화하려면 i와 j 사이의 모든 강의도 같은 블루레이에 녹화해야 한다.
#
# 강토는 이 블루레이가 얼마나 팔릴지 아직 알 수 없기 때문에, 블루레이의 개수를 가급적 줄이려고 한다. 오랜 고민 끝에 강토는 M개의 블루레이에 모든 기타 강의 동영상을 녹화하기로 했다. 이때, 블루레이의 크기(녹화 가능한 길이)를 최소로 하려고 한다. 단, M개의 블루레이는 모두 같은 크기이어야 한다.
#
# 강토의 각 강의의 길이가 분 단위(자연수)로 주어진다. 이때, 가능한 블루레이의 크기 중 최소를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 강의의 수 N (1 ≤ N ≤ 100,000)과 M (1 ≤ M ≤ N)이 주어진다. 다음 줄에는 강토의 기타 강의의 길이가 강의 순서대로 분 단위로(자연수)로 주어진다. 각 강의의 길이는 10,000분을 넘지 않는다.
#
# 출력
# 첫째 줄에 가능한 블루레이 크기중 최소를 출력한다.
#
# 시간 제한 2s

# 레슨에서 가장 길이가 긴 레슨을 start(그러면 더 짧은 레슨도 당연히 저장 가능), 레슨 길이의 합을 end

# 입력
N, M = map(int, input().split())

lesson_time = list(map(int, input().split()))
# lesson_time.sort()

# 그냥 이렇게 하면 돼
start = max(lesson_time)
end = sum(lesson_time)

# start > end: 탐색 끝
while start <= end:
    middle = int((start + end) / 2)
    # lesson_time의 총합
    sum = 0
    # 필요한 블루레이 개수
    current_count = 0

    # 최대 강의의 수 N까지
    for i in range(N):
        # 여기 두면 if check없이 일단 더하기 떄문에 안돼
        # sum += lesson_time[i]

        # 이 경우에는 필요 블루레이 개수 current_count + 1하고 sum을 초기화 해야함(개수 하나를 올렸잖아!)
        if sum + lesson_time[i] > middle:
            current_count += 1
            sum = 0
            
        sum += lesson_time[i]

    # sum != 0이 아니라면 블루레이가 하나 더 필요함
    if sum != 0:
        current_count += 1

    # 현재 필요한 블루레이 개수가 가지고 있는 블루레이 개수보다 크면
    if current_count > M:
        start = middle + 1
    else:
        end = middle - 1

# BS 종료되었을 때, start가 블루레이 크기 중 최소값
# 왜지 이해가 안되네 start > end 일 때 그 값(start)이 최소값이라..?
print(start)


