def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def lcm(a, b):
    return a * b // gcd(a, b)

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    print(lcm(x, y))