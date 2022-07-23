word = input()
suffix_list = []

for i in range(len(word)):
    suffix = word[i::]
    suffix_list.append(suffix)

suffix_list.sort()
print('\n'.join(suffix_list))