s = input()

encrypted = ''

for i in range(len(s)):
    if s[i].isalpha():
        # 아스키 코드 활용
        if (ord(s[i])>64 and ord(s[i])<78) or (ord(s[i])>96 and ord(s[i])<110):
            encrypted += chr(ord(s[i]) + 13)
        else:
            encrypted += chr(ord(s[i]) - 13)
    else:
        encrypted += s[i]

print(encrypted)