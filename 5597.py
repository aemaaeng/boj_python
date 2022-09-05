# 과제 안 내신 분...?

# 1번부터 30번까지 저장
students = [x for x in range(1, 31)]

for _ in range(28):
    i = int(input())

    # 제출한 사람은 리스트에서 지우기
    if i in students:
        students.remove(i)

# 남은 사람 (= 미제출자) 출력
for missing in students:
    print(missing)
