# 수 이어 쓰기 1

# 0 ~ 9 -> 똑같음
# 5 -> 12345
# 10 ~ 99 
# 9 + 6*2  = 21 (15)
# 100 ~ 999
# 9 + 90*2 + 21*3 = 252 (99 + 21 = 120)
# 1000 ~ 9999
# 9 + 90*2 + 900*3 + ...
# 10000 ~ 99999
# 9 + 90*2 + 900*3 + 9000*4 + ....

n = input() # 15
digits = 0
rest = 0

if int(n) >= 10:
    for i in range(0, len(n) - 1):
        digits += 9 * (10 ** i) * (i + 1)
        rest += 9 * (10 ** i)
    digits += (int(n) - rest) * len(n)
    print(digits)
else:
    print(int(n))
