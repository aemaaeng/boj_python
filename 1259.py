while True:
    check = input()
    if check == '0':
        break
    else:
        if check == ''.join(reversed(check)):
            print('yes')
        else:
            print('no')