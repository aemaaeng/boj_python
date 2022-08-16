# Hashing - 딕셔너리로 풀기
m = 1234567891
r = 31

alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = {}

for i in range(len(alpha)):
    num[alpha[i]] = i + 1

L = int(input())
str = input()

def hash_mod(s):
    seq = 0
    for j in range(len(s)):
        seq += num[s[j]] * (r ** j)
    res = seq % m
    return res

print(hash_mod(str))
