import sys
n = int(sys.stdin.readline())
members = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append([int(age), name])

# 각 첫 번째 인덱스를 기준으로 정렬
members.sort(key=lambda x:x[0])

for info in members:
    print(info[0], info[1])