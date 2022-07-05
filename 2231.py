n = int(input())
sums = []

for num in range(1, n + 1):
    sum = num
    s = str(num)
    for j in s:
        sum += int(j)
    if sum == n:
        sums.append(num)

if len(sums) == 0:
    print(0)
else:
    print(min(sums))