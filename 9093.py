# 단어 뒤집기

for _ in range(int(input())):
    s = list(input().split())
    reverse_s = []
    for chunk in s:
        stack = []
        word = ''
        for i in range(len(chunk)):
            stack.append(chunk[i])
        for j in range(len(stack)):
            word += stack.pop() # 팝도 반복해야됨. 
        reverse_s.append(word)
    print(' '.join(reverse_s))
