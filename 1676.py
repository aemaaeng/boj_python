n = int(input())

# 0은 5의 배수일 때 무조건 나타남
# 따라서 해당 수의 인수에서 5로 나눠떨어지는 수의 개수 세기
def five_cnt(n):
    cnt = 0
    while n != 0:
        n = n // 5
        cnt += n
    return cnt

print(five_cnt(n))