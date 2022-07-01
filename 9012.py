for _ in range(int(input())):  # 테스트케이스 개수 입력 받기
    sum = 0
    par = input()  # 괄호 입력 받기

    for p in par:
        if p == "(":  # 왼쪽 괄호라면 1 더해주기
            sum += 1
        else:
            sum -= 1  # 오른쪽 괄호가 나오면 sum에서 1 빼주기
        if sum < 0:  # sum이 음수가 되면 반복문 빠져나오기
            break

    if sum == 0:  # sum이 0일 경우에만 YES 출력
        print("YES")
    else:  # sum이 양수이거나 음수인 경우에는 전부 NO
        print("NO")