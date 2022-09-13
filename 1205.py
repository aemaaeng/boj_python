# 등수 구하기
# 각각의 노래마다 랭킹 리스트가 있다. 내림차순으로 저장됨
# p = 점수의 개수, 리스트에 있는 점수 n개, 태수의 점수
import sys
n, record, p = map(int, sys.stdin.readline().split())

scores = []

if n:
    scores = list(map(int, sys.stdin.readline().split()))
    scores.append(record)
    scores = sorted(scores, reverse=True)
    idx = scores.index(record) + 1
    if idx > p:
        print(-1)
    else:
        if n == p and record == scores[-1]:
            print(-1)
        else:
            print(idx)
else:
    print(1)
