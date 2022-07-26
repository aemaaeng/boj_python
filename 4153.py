while True:
    line = list(map(int, input().split()))
    if sum(line) == 0:
        break
    max_line = max(line)
    line.remove(max_line)
    if line[0]**2 + line[1]**2 == max_line**2:
        print('right')
    else:
        print('wrong')