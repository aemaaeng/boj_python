import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
cnt = 0

for _ in range(n):
    i = int(input())
    coins.append(i)

coins.sort(reverse=True)  # 큰 가치의 동전부터 탐색

for coin in coins:
    cnt += k // coin
    k %= coin

print(cnt)