# 체스판 다시 칠하기
from re import M


n, m = map(int, input().split())
board = []
cnt = []

for _ in range(n):
    board.append(input())
    
# 8*8로 cut
for x in range(n - 7):
    for y in range(m - 7):
        idx1 = 0
        idx2 = 0
        for i in range(x, x + 8):
            for j in range(y, y + 8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        idx1 += 1
                    if board[i][j] != 'B':
                        idx2 += 1
                else:
                    if board[i][j] != 'B':
                        idx1 += 1
                    if board[i][j] != 'W':
                        idx2 += 1
        cnt.append(min(idx1, idx2))

print(min(cnt))
