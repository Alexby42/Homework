def all_variants(string):
    for start in range(len(string)):
        for end in range(start + 1, len(string) + 1):
            yield string[start:end]
a = all_variants('abc')
for i in a:
    print(i)