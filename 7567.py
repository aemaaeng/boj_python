# 그릇
plates = input()

height = 0

for i in range(len(plates)):
    # 바닥에 놓인 첫 번째 그릇의 높이는 무조건 10
    if i == 0: 
        height += 10
    elif plates[i] == plates[i - 1]:
        height += 5
    else:
        height += 10

print(height)
