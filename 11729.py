def tower(n, start, other, dest):
    if n == 1:
        moves.append([start, dest])
    else:
        tower(n - 1, start, dest, other)
        moves.append([start, dest])
        tower(n - 1, other, start, dest)


moves = []
n = int(input())
tower(n, 1, 2, 3)

print(len(moves))
print('\n'.join([' '.join(str(i) for i in row) for row in moves]))
