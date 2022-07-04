n, m = map(int, input().split())  # 카드의 개수와 한도
cards = list(map(int, input().split()))  # 카드에 적힌 수
sum = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            total = cards[i] + cards[j] +cards[k]

            if sum < total and total <= m:
                sum = total

print(sum)