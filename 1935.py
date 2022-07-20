# 입력받기
n = int(input())
postfix = input()

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
operand = {}
stack = []

# 각 알파벳에 대응하는 수 저장
for i in range(n):
    j = int(input())
    operand[alpha[i]] = j

for token in postfix:
    if token.isalpha():
        stack.append(operand[token])
    
    elif token in '+-*/':
        a = stack.pop()
        b = stack.pop()
        
        if token == '+':
            stack.append(b + a)
        if token == '-':
            stack.append(b - a)
        if token == '*':
            stack.append(b * a)
        if token == '/':
            stack.append(b / a)

# 소수점 둘째자리까지 무조건 출력해야 함.            
result = '{:.2f}'.format(round(stack.pop(), 2))

print(result)
