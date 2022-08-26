# 약수들의 합

while True:
    num = int(input())
    divisor = []

    # -1일 때에는 반복문 중지
    if num == -1:
        break

    # 약수를 찾아 리스트에 저장
    for i in range(1, num):
        if num % i == 0:
            divisor.append(i)

    # 약수들의 합이 n과 같은지 판단하고 결과 출력하기
    if sum(divisor) == num:
        res = "{} = {}".format(num, divisor[0])

        # 약수 덧붙이기
        for j in range(1, len(divisor)):
            res = res + " + {}".format(divisor[j])
        
        print(res)
    else:
        print("{} is NOT perfect.".format(num))
