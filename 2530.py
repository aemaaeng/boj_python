# 인공지능 시계
hour, min, sec = map(int, input().split())
cooking_sec = int(input())

sec += cooking_sec
min += sec // 60
hour += min // 60

print(hour % 24, min % 60, sec % 60)