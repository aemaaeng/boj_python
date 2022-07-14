s = input()
stack = []
res = ""
tag = False

for i in s:
    # 태그일 때
    if i == "<":
        # 스택에 남은 문자를 팝
        while stack:
            res += stack.pop()
        tag = True
        res += i  # 팝한 후에 "<" 덧붙이기
        continue  # 아래 코드는 실행하지 않음
    elif i == ">":
        res += i
        tag = False
        continue
    
    if tag:  # "<>" 안의 문자라면
        res += i  # 바로 결과 문자열에 넣는다
    else:
        if i != " ":
            stack.append(i)
        else:
            while stack:
                res += stack.pop()
            res += i  # 공백 삽입

# 스택에 남아있는 문자열 처리하기
while stack:
    res += stack.pop()

print(res)