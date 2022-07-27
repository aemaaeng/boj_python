notation = list(input())

stack = []
result = []

# 연산자의 우선순위 지정
prec = {}
prec['('] = 0
prec['+'] = 1
prec['-'] = 1
prec['*'] = 2
prec['/'] = 2

for token in notation:
    # 연산자
    if token == '(':
        stack.append(token)
    elif token == ')':
        while stack[-1] != '(':
            popped = stack.pop()
            result.append(popped)
        stack.pop()
    elif token in '+-*/':
        if len(stack) == 0:
            stack.append(token)
        else:
            if prec[token] <= prec[stack[-1]]:
                while len(stack) != 0 and prec[token] <= prec[stack[-1]]:
                    popped = stack.pop()
                    result.append(popped)
                stack.append(token)
            else:
                stack.append(token)
    else:  # 피연산자
        result.append(token)

# 스택에 남아있는 연산자 처리
while len(stack) != 0:
    result.append(stack.pop())

# 후위표기식 완성
print("".join(result))