# 대소문자 바꾸기

text = input()
new = ''

for s in text:
    if s.isupper():
        s = s.lower()
        new += s
    else:
        s = s.upper()
        new += s

print(new)
