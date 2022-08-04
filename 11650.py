import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    lst.append([x, y])

lst.sort(key=lambda x:x[1])
lst.sort(key=lambda x:x[0])

for co in lst:
    print(co[0], co[1])