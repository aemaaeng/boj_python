# 베스트셀러
n = int(input())

sales = {}

for _ in range(n):
    book = input()
    if book not in sales.keys():
        sales[book] = 0
    sales[book] += 1

# 많이 팔린 책이 여러 개일 경우 사전순으로 가장 앞서는 제목 출력
keys = list(sales.keys())
keys.sort()
top = sales[keys[0]]
title = keys[0]

for k in range(len(keys)):
    if top < sales[keys[k]]:
        top = sales[keys[k]]
        title = keys[k]

print(title)