# 약수
import sys

M = int(sys.stdin.readline())
divisor = list(map(int, sys.stdin.readline().split()))

divisor.sort()

N = divisor[0] * divisor[-1]

print(N)
