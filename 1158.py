from collections import deque
import sys

n , k = map(int, sys.stdin.readline().split())
D = deque()
josephus = []

# n까지 큐에 넣기
for i in range(1, n + 1):
    D.append(i)

# k번째 원소는 팝하여 josephus 리스트에 삽입
while len(D) > 0:
    for j in range(1, k):
        D.append(D.popleft())
    josephus.append(str(D.popleft()))

# 출력 양식에 맞게 코드 작성
print("<{}>".format(', '.join(josephus)))