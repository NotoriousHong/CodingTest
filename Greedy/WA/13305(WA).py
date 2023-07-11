# n : 도시의 개수
# distances : 도시 사이의 거리(n-1개)
# gasPrice : 주유소 리더탕 가격

import sys

n = int(sys.stdin.readline())
distances = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))

# 양 끝 점을 제외한 gasPrice 중 제일 값이 싼 지점을 찾는다
# 해당 지점 기준 오른쪽 distance를 모두 커버할 수 있게 해당 지점 주유소에서 기름을 산다
# 두번째로 싼 주유소를 왼쪽에서 찾는다
# 계속 찾다가 찾는 값이 list의 두번쨰 요소가 되면 탈출한다


min_gasPrice = min(gasPrice[1:-1])
min_gasPrice_index = gasPrice.index(min_gasPrice)

result = 0

for i in range(min_gasPrice_index, len(distances)):
    result += min_gasPrice * distances[i]

min_gasPrice = min(gasPrice[1:min_gasPrice_index])
min_gasPrice_index = gasPrice.index(min_gasPrice)


#! 문제에서 도시의 개수가 100,000이하의 자연수 였음으로 해당 문제는 내가 위에 작성한 코드와 같이 재귀적으로 구현해서 풀 수 없다.
