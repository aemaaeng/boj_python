# Hashing - 아스키코드 활용
L = int(input())
str = input()
res = 0

for i in range(L):
    res += (ord(str[i]) - 96) * (31 ** i)

res = res % 1234567891
print(res)
