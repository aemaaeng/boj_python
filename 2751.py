import sys
n = int(sys.stdin.readline())
lst = []

for i in range(n):
    i = int(sys.stdin.readline())
    lst.append(i)

lst = sorted(lst)

for j in lst:
    print(j)