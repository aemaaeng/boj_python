# 통계학
import sys
from collections import Counter

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    i = int(sys.stdin.readline())
    nums.append(i)

nums.sort()

avg = round(sum(nums) / n)
ran = max(nums) - min(nums)

def mode(lst):
    c = Counter(lst)
    cnt = c.most_common()
    m = cnt[0][1]
    modes = []
    for j in cnt:
        if j[1] == m:
            modes.append(j[0])
    modes.sort()
    if len(modes) < 2:
        return modes[0]
    else:
        return modes[1]

if len(nums) < 2:
    med = nums[0]
else:
    med = nums[n // 2]


stat = [avg, med, mode(nums), ran]
print(*stat, sep ='\n')
