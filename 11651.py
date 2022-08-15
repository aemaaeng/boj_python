import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

# y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순으로 정렬
lst.sort(key=lambda x:x[0])
lst.sort(key=lambda x:x[1])

for co in lst:
    print(co[0], co[1])
