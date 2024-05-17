import random
n = random.randint(3, 20)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(n)
for i in range(0, len(numbers)):
    for j in range(i + 1, len(numbers)):
        if n % (numbers[i] + numbers[j]) == 0:
            summa = numbers[i], numbers[j]
            result = ''.join(map(str, summa))
            print(result, end="")