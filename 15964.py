def compute(num1, num2):
    result = (num1 + num2) * (num1 - num2)
    return result

A, B = map(int, input().split())
print(compute(A, B))
