import sys

n = int(sys.stdin.readline())
words = []

for _ in range(n):
    word = sys.stdin.readline().rstrip()
    words.append(word)

# 중복 제거
words_set = set(words)
words = list(words_set)

# 알파벳 순 정렬
words.sort()

# 길이순 정렬
words.sort(key=len)
print('\n'.join(words))