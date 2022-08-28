# 중복 빼고 정렬하기

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

nums = list(set(nums))
nums.sort()

print(*nums)
