n = int(input())
time = list(map(int, input().split()))

time.sort()
sum = 0

for i in range(1, len(time) + 1):
    for j in range(i):
        sum += time[j]

print(sum)