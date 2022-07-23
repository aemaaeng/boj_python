serial = list(map(int, input().split())) 
sum = 0

for s in serial:
    sum += s ** 2

print(sum % 10)