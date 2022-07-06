data = []
ranks = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(len(data)):
    # 자신보다 큰 사람이 없을 땐 1등이므로 초기값을 1로 설정
    cnt = 1
    for j in range(len(data)):
        # 자신보다 큰 사람의 수 세기
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            cnt += 1
    ranks.append(cnt)

for r in ranks:
    print(r, end=" ")