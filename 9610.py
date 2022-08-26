# 사분면
q1 = 0
q2 = 0
q3 = 0
q4 = 0
axis = 0

for _ in range(int(input())):
    x, y = map(int, input().split())

    # AXIS: x 또는 y가 0
    if y == 0 or x == 0:
        axis += 1
    
    # Q1: x도 양수, y도 양수
    elif x > 0 and y > 0:
        q1 += 1
    
    # Q2: x는 음수, y는 양수
    elif x < 0 and y > 0:
        q2 += 1

    # Q3: x도 음수, y도 음수
    elif x < 0 and y < 0:
        q3 += 1
    
    # Q4: x는 양수, y는 음수
    elif x > 0 and y < 0:
        q4 += 1
    

print("Q1: %d" %(q1))
print("Q2: %d" %(q2))
print("Q3: %d" %(q3))
print("Q4: %d" %(q4))
print("AXIS: %d" %(axis))

