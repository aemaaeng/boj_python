import sys

n = int(sys.stdin.readline())
deq = []

for i in range(n):
    cmd = sys.stdin.readline().split()
    
    if cmd[0] == 'push_front':
        deq.insert(0, int(cmd[1]))
    if cmd[0] == 'push_back':
        deq.append(int(cmd[1]))
    if cmd[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop(0))
    if cmd[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop(-1))
    if cmd[0] == 'size':
        print(len(deq))
    if cmd[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    if cmd[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    if cmd[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])