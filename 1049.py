# 기타줄

# 끊어진 기타줄의 개수, 기타줄 브랜드
n, m = map(int, input().split())
sets = []
ones = []
six_ones = []

for _ in range(m):
    set, one = map(int, input().split())
    sets.append(set)
    ones.append(one)
    six_ones.append(one * 6)

min_ones = min(ones)
min_sets = min(sets)
min_six = min(six_ones)

if n <= 6:
    print(min(min_ones * n, min_sets))
else:
    print(min(min_sets, min_six) * (n // 6) + min(min_ones * (n % 6), min_sets))
