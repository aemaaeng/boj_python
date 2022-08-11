# 프린터 큐
for _ in range(int(input())):
    # N = 문서의 개수, M = 문서가 Queue에 놓인 순서
    N, M = map(int, input().split())
    
    # N개 문서의 중요도
    prec = list(map(int, input().split()))
    idx = list(range(N))
    idx[M] = 'target'
    
    # 문서가 출력될 순서
    order = 0

    while True:
        if prec[0] == max(prec):
            order += 1

            if idx[0] == 'target':
                print(order)
                break
            else:
                prec.pop(0)
                idx.pop(0)
        else:
            prec.append(prec.pop(0))
            idx.append(idx.pop(0))
