# 그대로 출력하기

while True:
    try:
        print(input())
    except EOFError:
        break

# sys를 활용한 코드는 EOFError를 발생시키지 않아 오답처리 되었다.
