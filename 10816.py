import sys
ipt = sys.stdin.readline

n = int(ipt())
cards = [*map(int, ipt().split())]
m = int(ipt())
check = [*map(int, ipt().split())]

count = {}

# 카드의 개수 세서 딕셔너리에 담기
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

# 살펴볼 값들을 딕셔너리의 value에서 탐색
for val in check:
    res = count.get(val)
    if res == None:
        print(0, end=" ")
    else:
        print(res, end=" ")
