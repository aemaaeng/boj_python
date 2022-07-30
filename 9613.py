import itertools

def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b

for _ in range(int(input())):
    nums = list(map(int, input().split()))
    cnt = nums[0]
    nums.remove(nums[0])
    combi = list(itertools.combinations(nums, 2))
    gcd_list = []
    
    for i in range(len(combi)):
        a, b = combi[i][0], combi[i][1]
        gcd_list.append(gcd(a, b))
    
    print(sum(gcd_list))