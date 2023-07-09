import sys
import math

# t = 케이스의 개수
# x1, y1, r1(조규현)
# x2, y2, r2(배승환)
t = int(sys.stdin.readline())

count = 0

while count < t:
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 두 원의 중심 사이의 거리
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

    # 원의 좌표가 같은 경우
    if distance == 0:
        # 좌표가 같고 마린과의 거리가 같은 경우(두 원이 같은 좌표에 존재하고 반지름 길이도 일치함, 같은 원임)
        if r1 == r2:
            print(-1)
        # 좌표가 같지만 마린과의 거리가 다른 경우(원 내부에 원이 존재하여 접점이 없음)
        else:
            print(0)
    # 원의 좌표가 다른 경우, 접점이 1개이거나 2개
    else:
        # 두 원의 중심좌표 사이의 거리와 r1 + r2 거리가 같은 경우(외부에서 접점 1개 만남)
        # or
        # 두 원의 중심좌표 사이의 거리와 r2 - r1 거리가 같은 경우(내부에서 접점 1개 만남)
        if r1 + r2 == distance or abs(r2 - r1) == distance:
            print(1)
        # 두 원의 중심좌표 사이의 거리가 r1 - r2의 절댓값과 r1 + r2 사이에 있는 경우(접점 2개)
        elif ((abs(r1 - r2) < distance) and (distance < r1 + r2)):
            print(2)
        # 두 원의 중심좌표 사이의 거리가 r1 + r2보다 커서 접점이 없는 경우
        else:
            print(0)
    count += 1
