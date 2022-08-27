# 숫자 카드
import sys

# input
N = int(sys.stdin.readline())
cards = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

dict = {}

# 딕셔너리에 카드 매핑
for i in range(len(cards)):
    dict[cards[i]] = 0

# 체크하기
for j in range(M):
    if nums[j] in dict:
        print(1, end=' ')
    else:
        print(0, end=' ')
