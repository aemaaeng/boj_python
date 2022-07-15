# 쇠막대기
bars = input()
stack = []
cnt = 0

for i in range(len(bars)):
    if bars[i] == '(':  # '('는 무조건 스택에 append
        stack.append(bars[i])
    else:  # ')'일 때에는 두 경우로 나뉨.
        if bars[i - 1] == '(':  # 전 문자가 '('였으면 레이저라는 의미
            stack.pop()  # ')'의 짝이 되는 '('는 팝
            cnt += len(stack)  # 나머지 쇠막대기의 개수 더하기
        else:
            stack.pop()  # 전 문자도 '('라면 쇠막대기의 끝이라는 의미.
            cnt += 1  # 끄트머리가 나올 때마다 1씩 더하기
            
print(cnt)