# 온라인 판매
# 최대 수익을 올릴 수 있는 달걀의 가장 낮은 가격 책정
# n = 달걀 개수 m = 잠재적인 고객 수
n, m = map(int, input().split())
prices = []

for _ in range(m):
    prices.append(int(input()))
prices = sorted(prices, reverse=True)

price = 0
max_profit = 0

for i in range(m):
    if i + 1 > n:
        profit = prices[i] * n
    else:
        profit = prices[i] * (i + 1)
    
    if max_profit < profit:
        price = prices[i]
        max_profit = profit

print(price, max_profit)
