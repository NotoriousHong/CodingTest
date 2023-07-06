# n = 상품 수, m = 고객 수
n, m = map(int, input().split())

# a = 상품의 만족도, b = 고객의 지불비용   #  lambda x : 반환하는 값 형태, x로 들어온 입력값을 처리하는 방법
a = list(map(int, input().split())) # map(lambda x: int(), sys.stdin.readline().split())
b = list(map(int, input().split())) # map(lambda x: int(), sys.stdin.readline().split())

# a를 내림차순, b를 오름차순 정렬
a.sort(reverse=True)
b.sort()

# 상품 만족도는 최상 지불비용은 최저
# 각 고객에세 상품을 매치
# 상품 만족도 가장 높은 물품 -> 가장 낮은 지불의사를 가진 고객에게 매치

result = 0

# b리스트의 length가 끝날 때까지 for문 반복
for i in range(min(n, m)):
    if a[i] - b[i] <= 0:
        continue
    result += a[i] - b[i]

print(result)