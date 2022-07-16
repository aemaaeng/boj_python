word = input()
alpha = 'abcdefghijklmnopqrstuvwxyz'

cnt = [0] * 26

for s in word:
    idx = alpha.index(s)
    cnt[idx] += 1

print(*cnt)