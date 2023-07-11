# 물이 새는 곳의 개수 n
# 테이프의 길이 L


# 입력받는 누수 위치를 오름차순으로 정렬한다
# for문을 통해 누수 위치를 순서대로 순회한다
# 만약 '누수 위치 사이의 누적된 간격 >= 테이프의 길이'라면 필요한 테이프 개수 +1
# 누수 위치 사이의 누적된 간격 초기화

n, l = map(int, input().split())
leak_location = list(map(int, input().split()))


sorted_leak_location = sorted(leak_location)

distance = 0
result = 1
i = 1

while i < len(sorted_leak_location):

    distance += sorted_leak_location[i] - sorted_leak_location[i-1]

    # distance = 3
    # i = 3

    if distance >= l:
        result += 1
        distance = 0
    i += 1


while i < len(sorted_leak_location):

    if distance <= l:
        distance += sorted_leak_location[i] - sorted_leak_location[i-1]

        # 위 코드를 그대로 쓰면서 올바르게 작동할려고 한다면 위 if문 안에서 아래 조건을 추가해줘야 함
        # if distance > l:
        #         result += 1
        #         distance = 0

    # 잘못된 scope
    else:
        result += 1
        distance = 0
    i += 1


print(result)
