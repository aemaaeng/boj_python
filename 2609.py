x, y = map(int, input().split())

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(x, y))
print(lcm(x, y))