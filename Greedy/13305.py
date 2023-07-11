# n : 도시의 개수
# distances : 도시 사이의 거리(n-1개)
# gasPrice : 주유소 리더탕 가격

import sys

n = int(sys.stdin.readline())
distances = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))

# 왼쪽에서 오른쪽으로 도로를 이동한다고 할 때
# 최적의 gasPrice값을 설정하는 변수 하나를 지정한다(처음 출발할 때는 첫번째 도시의 gasPrice가 최적값이 된다)
# 오른쪽으로 한칸 이동하며 최적의 gasPrice와 distance를 곱한다

optimal_gasPrice = gasPrice[0]
result = 0

for i in range(n-1):
    # 만약 현재 최적 gasPrice가 다음 gasPrice보다 크다면
    if optimal_gasPrice > gasPrice[i + 1]:
        result += optimal_gasPrice * distances[i]
        optimal_gasPrice = gasPrice[i + 1]
    # 다음 gasPrice가 더 작다면 현재 값을 쭉 가지고 가면서 result에 더해준다
    else:
        result += optimal_gasPrice * distances[i]

print(result)
