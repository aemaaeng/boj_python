# 부녀회장이 될테야
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    # 0층은 고정
    f0 = [x for x in range(1, n + 1)]

    # 0층을 베이스로 층수가 증가할 때마다 사람 수 더하기
    for i in range(k):
        for j in range(1, n):
            f0[j] += f0[j - 1]
    
    print(f0[-1])
