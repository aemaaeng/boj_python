# 초콜릿 자르기
n, m = map(int, input().split())

cnt = 1  # 초콜릿의 개수
cut = 0  # 쪼갠 횟수

while cnt < n * m:
    cut += 1
    cnt += 1

print(cut)
