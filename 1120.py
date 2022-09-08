# 문자열

# 두 문자열의 차이는 X[i] != Y[i]인 i의 개수
# X = 'jimin' Y = 'minji' -> 4

a, b = input().split()  # adaabc aababbc
res = []

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i + j]:
            cnt += 1
    res.append(cnt)

print(min(res))

# i가 커질 때마다 문자열 a가 한 칸씩 밀림!
# i = 0 -> 4
# koder
# topcoder
# i = 1 -> 5
#  koder
# topcoder
# i = 2 -> 5
#   koder
# topcoder
# i = 3 -> 1
#    koder
# topcoder
