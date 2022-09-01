# TGN
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    r, e, c = map(int, sys.stdin.readline().split())

    if r + c > e:
        print("do not advertise")
    elif r + c < e:
        print("advertise")
    else:
        print("does not matter")
