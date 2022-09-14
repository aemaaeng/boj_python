# 듣보잡
n, m = map(int, input().split())
neverheard = {}
neverseen = {}

# 듣도 못한 사람
for _ in range(n):
    neverheard[input()] = 1

# 보도 못한 사람
for _ in range(m):
    name = input()
    if name in neverheard.keys():
        neverheard[name] += 1
    else:
        neverseen[name] = 1

both = []

# neverheard에서 value가 2인 것들의 key만 뽑아내어 both 리스트에 넣기
for key, value in neverheard.items():
    if value == 2:
        both.append(key)

both = sorted(both)

print(len(both), *both, sep='\n')
