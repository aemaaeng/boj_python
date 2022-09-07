# 라디오
a, b = map(int, input().split())

favorites = []

# N개의 줄만큼 즐겨찾기 주파수 입력받기
for _ in range(int(input())):
    favorites.append(int(input()))

min_value = 1001
freq = 0

# 반복문 돌며 최솟값으로 만들어주는 즐겨찾기 주파수 찾기
for i in favorites:
    # 최솟값을 저장하는 임시 변수
    temp = abs(i - b)
    if min_value > temp:
        min_value = temp
        # 최솟값으로 만들어주는 즐겨찾기 주파수 저장
        freq = i

# 주파수를 일일이 누른 값 -> abs(a - b)
# 즐겨찾기로 찾아서 누른 값 -> abs(즐겨찾기 주파수 - b) + 1
# 둘을 비교하여 최솟값 리턴
print(min(abs(a - b), (abs(freq - b) + 1)))
