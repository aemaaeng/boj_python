# 명령 프롬프트

N = int(input())
first_file = list(input())

for _ in range(N - 1):
    other_files = list(input())
    for i in range(len(first_file)):
        if first_file[i] != other_files[i]:
            first_file[i] = '?'

print(''.join(first_file))
