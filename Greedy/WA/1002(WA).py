import sys
import math

# t = 케이스의 개수
# x1, y1, r1(조규현)
# x2, y2, r2(배승환)
t = int(sys.stdin.readline())

case = []
result = []
count = 0

while count < t:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    case.append([x1, y1, r1, x2, y2, r2])
    count += 1


for i in range(len(case)):
    # case의 첫째 요소부터 순회한다
    # case[i][0] : x1
    # case[i][1] : y1
    # case[i][2] : r1
    # case[i][3] : x2
    # case[i][4] : y2
    # case[i][5] : r2

    distance_squared = pow(case[i][0] - case[i][3], 2) + \
        pow(case[i][1] - case[i][4], 2)
    sum_of_radii_squared = pow(case[i][2] + case[i][5], 2)
    jo_location = f"{case[i][0]}, {case[i][1]}"
    bae_location = f"{case[i][3]}, {case[i][4]}"
    jo_marine_distance = f"{case[i][2]}"
    bae_marine_distance = f"{case[i][5]}"

    # 규현과 승환의 좌표가 일치하고 마린과 떨어져 있는 거리가 일치하지 않는 경우
    if jo_location == bae_location and jo_marine_distance != bae_marine_distance:
        result.append(0)
    # 규현과 승환의 좌표가 일치하고 마린과 떨어져 있는 거리가 일치하는 경우
    elif jo_location == bae_location and jo_marine_distance == bae_marine_distance:
        result.append(-1)
    # 피타고라스 정의로 구한 규현과 승환 사이 거리의 합이 규현과 승환이 마린과 떨어져 있는 거리와 같은 경우(원이 1개 겹침)
    elif distance_squared == sum_of_radii_squared:
        result.append(1)
    # 피타고라스 정의로 구한 규현과 승환 사이 거리의 합이 규현과 승환이 마린과 떨어져 있는 거리보다 작은 경우(원이 2개 겹침)
    elif distance_squared < sum_of_radii_squared:
        result.append(2)
    # 피타고라스 정의로 구한 규현과 승환 사이 거리의 합이 규현과 승환이 마린과 떨어져 있는 거리보다 큰 경우(원이 0개 겹침)
    else:
        result.append(0)

for element in result:
    print(element)
