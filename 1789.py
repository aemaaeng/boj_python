# 수들의 합
s = int(input())
sum = 0
cnt = 0

while True:
    cnt += 1
    sum += cnt
    if sum > s:
        print(cnt - 1)
        break
