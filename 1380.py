# 귀걸이

def rings(n):
    girls = [input() for _ in range(n)]
    earrings = {}

    for _ in range(2*n - 1):
        number, alpha = input().split()
        earrings[number] = earrings.get(number, 0) + 1

    for key, val in earrings.items():
        if val == 1:
            return girls[int(key) - 1]

scenario = 1
while True:
    n = int(input())
    if n == 0:
        break
    print(scenario, rings(n))
    scenario += 1
