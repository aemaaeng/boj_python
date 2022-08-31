# 영수증
import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())

sum = 0

for _ in range(N):
    price, count = map(int, sys.stdin.readline().split())
    sum += price * count

if sum == X:
    print('Yes')
else:
    print('No')
