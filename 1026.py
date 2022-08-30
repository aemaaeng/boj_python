# 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum = 0

while A and B:
    sum += min(A) * max(B)
    A.pop(A.index(min(A)))
    B.pop(B.index(max(B)))

print(sum)