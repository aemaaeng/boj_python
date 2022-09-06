# 쉽게 푸는 문제
lst = [0]
a, b = map(int, input().split())

# 이중반복문으로 수열 만들기
for i in range(46):
    for j in range(i):
        lst.append(i)

# 슬라이싱으로 합 구하기
print(sum(lst[a:b+1]))
