n = int(input())
process = []
stack = []
ok = True  # 수열 생성 가능 여부를 저장
cur = 1  # 1부터 오름차순으로 스택에 push

for _ in range(n):
    i = int(input())
    while cur <= i:  # i와 같을 때까지만 push
        stack.append(cur)
        process.append('+')
        cur += 1
    if i == stack[-1]:  # stack의 마지막 값과 i가 같다면 pop
        stack.pop()
        process.append('-')
    else:
        ok = False

if ok:
    print('\n'.join(process))
else:
    print('NO')
