# 메시지
cycle = 1

while True:
    n = int(input())

    if n == 0:
        break

    group = []

    for _ in range(n):
        paper = list(input().split())
        group.append(paper)
    
    nasty = []

    for i in range(n):
        for j in range(1, n):
            if group[i][j] == 'N':
                b = group[i][0]
                if j <= i:
                    a = group[i - j][0]
                else:
                    a = group[n + i - j][0]
                caught = '{} was nasty about {}'.format(a, b)
                nasty.append(caught)
    
    print('Group {}'.format(cycle))

    if len(nasty) == 0:
        print('Nobody was nasty')
    else:
        print(*nasty, sep='\n')
    
    print()
    cycle += 1

